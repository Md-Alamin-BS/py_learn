# /usr/bin/env python3
import argparse
import sys

from azure.ai.ml import MLClient
from azure.ai.ml.entities import ManagedOnlineEndpoint, IdentityConfiguration
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
    parser.add_argument("--endpoint-name", type=str, required=True)
    parser.add_argument(
        "--auth-mode",
        type=str,
        default="AADToken",
        required=False,
    )
    parser.add_argument(
        "--identity-type",
        type=str,
        default="SystemAssigned",
        required=False,
    )

    args = parser.parse_args()

    ml_client = MLClient(
        DefaultAzureCredential(),
        args.subscription_id,
        args.resource_group,
        args.aml_workspace,
    )

    existing_endpoints = ml_client.online_endpoints.list()
    matching_existing_endpoints = [
        e for e in existing_endpoints if e.name == args.endpoint_name
    ]

    if matching_existing_endpoints:
        # Preserve the current traffic allocation of the existing endpoint.
        # If we do not include the current traffic allocation in our create-or-update request,
        # it will be reset to the default value of 0%, causing downtime.
        #
        # To avoid this issue, we retrieve the existing endpoint that will contain the
        # current traffic allocation and update it with the new configuration.
        logger.info(f"Endpoint %s already exists. Updating it.", args.endpoint_name)
        endpoint = matching_existing_endpoints[0]
    else:
        logger.info("Endpoint %s does not exist. Creating it.", args.endpoint_name)
        endpoint = ManagedOnlineEndpoint(
            name=args.endpoint_name,
        )

    # Configure endpoint
    endpoint.auth_mode = args.auth_mode
    endpoint.identity = IdentityConfiguration(type=args.identity_type)

    # Create or update the endpoint
    try:
        ml_client.online_endpoints.begin_create_or_update(endpoint=endpoint).result()
    except Exception:
        logger.exception("Failed to provision endpoint.")
        raise

    logger.info("Endpoint provisioned successfully.")


if __name__ == "__main__":
    main()
