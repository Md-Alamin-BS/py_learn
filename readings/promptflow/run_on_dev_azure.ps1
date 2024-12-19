#!/usr/bin/env pwsh

# Enable strict mode and exit on error
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Generate current timestamp
$current_timestamp = Get-Date -Format "yyyyMMddHHmmss"

$run_id = "run_$current_timestamp"
$eval_id = "eval_$current_timestamp"
$data = "../../../../data/risk-tagging/reviewed_distributed_ddr_v5.csv"

$workspace = "mlw-dev-akerbpai"
$resource_group = "akerbp-ai-dev"
$subscription_id = "d6c4788f-bcf7-4967-9394-a358fb808e44"

# Create run for tag_record
pfazure run create -f flows/tag_record/batch_run.yaml --name $run_id --data $data --stream --workspace-name $workspace --resource-group $resource_group --subscription $subscription_id

# Create run for evaluation
pfazure run create -f flows/evaluation/batch_run.yaml --run $run_id --name $eval_id --data $data --stream --workspace-name $workspace --resource-group $resource_group --subscription $subscription_id

# Show metrics for evaluation
pfazure run show-metrics --name $eval_id --workspace-name $workspace --resource-group $resource_group --subscription $subscription_id