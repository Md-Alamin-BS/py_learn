# Prompt Flow flows

## Overview

We use Prompt Flow framework to define the tagging and evaluation algorithms as "flows".

These flows can be executed locally or on Azure Machine Learning (AML).
Additionally, they can be deployed as web services.

## Prerequisites

### Prepare virtual environment for prompt flow

1. Create virtual env

    ```bash
    python3 -m venv .venv
    ```

2. Activate virtual env

    E.g. for bash:

    ```bash
    source .venv/bin/activate
    ```

    Or powershell:

    ```bash
    ./.venv/Scripts/Activate.ps1
    ```

3. Install promptflow tooling:

    ```bash
    pip install -r dev_requirements.txt
    ```

### Service connection to Azure OpenAI

The inference flows include the Prompt Flow node of type `llm`, which handles querying the LLM.
This node uses a preconfigured [service connection](https://microsoft.github.io/promptflow/how-to-guides/manage-connections.html#) for authorization.
Ensure this service connection is set up on each platform where the flow will be executed.

The service connection name (`akerbp-ai`) and LLM model deployment name (`gpt-4o-mini`) are hardcoded in the flow definitions.
This means, you will need to create a service connection to Azure OpenAI with this name locally to run local inference flows,
and you need to have a model deployment with this name on this Azure OpenAI instance.

**To manually create the connection locally**, follow [this guide](https://microsoft.github.io/promptflow/how-to-guides/manage-connections.html#create-a-connection).
Although it's easier with the CLI, try to do it with the [PromptFlow VSCode extension](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow) in order to learn how this extension works.

On the VS Code primary sidebar > PromptFlow pane. You can find the connections pane to manage your local connections. Click the “+” icon on the top right of it and follow the popped out instructions to create your new connection.

![local_conn](../../docs/.attachments/azure_openai_conn.png)

**To manually create the connection on AML**, follow [this guide](https://learn.microsoft.com/azure/machine-learning/prompt-flow/get-started-prompt-flow?view=azureml-api-2#set-up-a-connection).
The connection to the Azure OpenAI instances `oai-dev-akerbpai` and `oai-test-akerbpai` are already created using the [CD pipeline](../../build/pipelines/cd-risk-tagging.yaml), so this step is not required if you use one of this.

## Running the flows

### Run locally

With virtualenv activated, you will have a `pf` utility available in the CLI.
Inspect the scipt [`run_locally.ps1`](./run_locally.ps1) to see how one can use `pf`.

Run the script [`run_locally.ps1`](./run_locally.ps1) in order to execute inference and evaluation locally.

Follow the links in the stdout logs to inspect the flow results.

### Run on Azure

With virtualenv activated, you will have a `pfazure` utility available in the CLI.
Inspect the scipt [`run_on_dev_azure.ps1`](./run_on_dev_azure.ps1) to see how one can use `pfazure`.

Run the script [`run_on_dev_azure.ps1`](./run_on_dev_azure.ps1) in order to execute inference and evaluation on Azure.
It will take more time than locally, but the results will be saved in the AML workspace.

Follow the links in the stdout logs to inspect the flow results.

## Develop the flows

Install the [Prompt Flow extension](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow) for VSCode.

Open the `flow.dag.yaml` file of an existing flow to work with it either in the visual editor or in the text editor a YAML file.
Using this extension, you can run and debug the flows in both extensions.

To create a new flow, you can either copy and adapt an existing flow or call the command `Prompt Flow: Create new flow` in VSCode.

### New standard flow

Our evaluation flow requires the results of a standard flow to be in a specific format.

To ensure accurate evaluation, please return all assessed tags in the following format:

```json
[
    {
        "tag": "string",
        "present": "boolean",
        "justification": "string | null"
    },
    {
        "tag": "string",
        "present": "boolean",
        "justification": "string | null"
    },
    ...
]
```

## Deployment

The flow can be deployed to a managed endpoint on AML.

Our deployment strategy follows the [official documentation](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-deploy-to-code) and the [LLMOps template](https://github.com/microsoft/genaiops-promptflow-template/tree/main/llmops/common/deployment).

To deploy a flow, use the script [`deploy_model.py`](./deployment/deploy_model.py). This script will create a new deployment, allocate all traffic to it, and remove old deployments.
