# /usr/bin/env python3
import argparse
import json
import random
import string
import sys

from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    ManagedOnlineDeployment,
    Environment,
    OnlineRequestSettings,
)
from azure.identity import DefaultAzureCredential
import logging

# Configure logger that will print to stdout
logger = logging.getLogger("deployment_logger")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def main():
    parser = argparse.ArgumentParser("Provision Deployment")
    parser.add_argument(
        "--subscription-id", type=str, help="Azure subscription id", required=True
    )
    parser.add_argument(
        "--resource-group", type=str, help="Resource group name", required=True
    )
    parser.add_argument(
        "--aml-workspace", type=str, help="AML workspace name", required=True
    )
    parser.add_argument(
        "--endpoint-name", type=str, help="AML endpoint name", required=True
    )
    parser.add_argument(
        "--model-name", type=str, help="Model to be deployed", required=True
    )
    parser.add_argument(
        "--model-version", type=str, help="Model version to be deployed", required=True
    )
    parser.add_argument(
        "--vm-size", type=str, help="VM SKU, e.g. Standard_DS3_v2", required=True
    )
    parser.add_argument(
        "--vm-count", type=int, help="How many VMs to deploy", required=True
    )

    args = parser.parse_args()

    ml_client = MLClient(
        DefaultAzureCredential(),
        args.subscription_id,
        args.resource_group,
        args.aml_workspace,
    )

    # ensure unique name to avoid in-place update of the deployment that might make it temporarily unavailable
    random_suffix = "".join(random.choices(string.ascii_lowercase, k=4))
    deployment_name = (
        f"{args.model_name}-v{args.model_version}-{random_suffix}".replace("_", "-")
    ).lower()  # deployment name must be lowercase

    # Create new deployment. Its default traffic allocation will be at 0%.
    create_deployment(ml_client, args, deployment_name)

    # Verify the new endpoint is valid before redirecting traffic to it.
    # See more about safe deployment practices at https://learn.microsoft.com/en-us/azure/machine-learning/how-to-safely-rollout-online-endpoints?view=azureml-api-2&tabs=azure-cli#confirm-your-existing-deployment
    if not test_deployment_works(ml_client, args.endpoint_name, deployment_name):
        logger.error("Deployment %s isn't functional. Deleting...", deployment_name)
        delete_deployment(ml_client, args.endpoint_name, deployment_name)
        sys.exit(1)  # return non-zero exit code from this script, signalling a failure

    # Update traffic allocation for the new deployment from 0% to 100%
    allocate_all_traffic(ml_client, args.endpoint_name, deployment_name)

    # Cleanup the previous deployments that don't receive traffic anymore
    cleanup_unused_deployments(ml_client, args.endpoint_name)


def create_deployment(ml_client, args, deployment_name):
    """
    Create new deployment on the endpoint.
    """
    environment_variables = {
        # PRT_CONFIG_OVERRIDE is required to use connections from the workspace
        # see https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-deploy-to-code?view=azureml-api-2&tabs=managed#define-the-deployment
        "PRT_CONFIG_OVERRIDE": (
            f"deployment.subscription_id={args.subscription_id},"
            f"deployment.resource_group={args.resource_group},"
            f"deployment.workspace_name={args.aml_workspace},"
            f"deployment.endpoint_name={args.endpoint_name},"
            f"deployment.deployment_name={deployment_name}"
        ),
    }

    environment = Environment(
        image="mcr.microsoft.com/azureml/promptflow/promptflow-runtime:20241031.v1",
        inference_config={
            "liveness_route": {"path": "/health", "port": "8080"},
            "readiness_route": {"path": "/health", "port": "8080"},
            "scoring_route": {"path": "/score", "port": "8080"},
        },
    )

    model = ml_client.models.get(args.model_name, args.model_version)

    deployment = ManagedOnlineDeployment(
        name=deployment_name,
        endpoint_name=args.endpoint_name,
        model=model,
        description="",
        environment=environment,
        instance_type=args.vm_size,
        instance_count=args.vm_count,
        environment_variables=environment_variables,
        tags={},
        app_insights_enabled=True,
        request_settings=OnlineRequestSettings(request_timeout_ms=90000),
    )

    logger.info("Creating deployment %s for model %s", deployment_name, args.model_name)
    ml_client.online_deployments.begin_create_or_update(deployment).result()


def test_deployment_works(ml_client, endpoint_name, deployment_name) -> bool:
    """
    Verify that the deployment is functional by sending a sample request and checking the response.
    Return True if the deployment works, False otherwise.
    """
    logger.info("Sending sample request to verify the deployment is functional...")
    try:
        response = ml_client.online_endpoints.invoke(
            endpoint_name=endpoint_name,
            request_file="./sample-request.json",
            deployment_name=deployment_name,
        )
    except Exception:
        logger.exception("Failed to invoke endpoint")
        return False

    logger.info("Response to sample request: %s", response)
    try:
        data = json.loads(response)  # response must be a valid JSON
    except Exception:
        logger.exception("Failed to deserialize response")
        return False

    if not (
        isinstance(data, dict) and "tags" in data and isinstance(data["tags"], list)
    ):
        logger.error("Response doesn't contain expected data")
        return False

    logger.info("Sample request succeeded")
    return True


def allocate_all_traffic(ml_client, endpoint_name, deployment_name):
    """
    Allocate all traffic to a single deployment.
    """
    logger.info("Allocating 100%% of traffic to the deployment %s", deployment_name)
    endpoint = ml_client.online_endpoints.get(endpoint_name)
    endpoint.traffic = {deployment_name: 100}
    ml_client.begin_create_or_update(endpoint).result()


def delete_deployment(ml_client, endpoint_name, deployment_name):
    logger.info("Deleting deployment %s...", deployment_name)
    ml_client.online_deployments.begin_delete(deployment_name, endpoint_name).result()


def cleanup_unused_deployments(ml_client, endpoint_name):
    """
    Delete all deployments that are not receiving 100% of the traffic.
    """
    endpoint = ml_client.online_endpoints.get(endpoint_name)
    operations = []
    for prior_deployment, traffic in endpoint.traffic.items():
        if traffic != 100:
            logger.info("Begin deleting deployment %s...", prior_deployment)
            operations.append(
                ml_client.online_deployments.begin_delete(
                    prior_deployment, endpoint_name
                )
            )

    if operations:
        logger.info("Waiting to delete %d unused deployments", len(operations))
        for operation in operations:
            operation.result()  # wait to finish

    logger.info("Deleted %d unused deployments", len(operations))


if __name__ == "__main__":
    main()
