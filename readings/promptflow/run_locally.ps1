#!/usr/bin/env pwsh

# Enable strict mode and set error action preference
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Generate current timestamp
$current_timestamp = Get-Date -Format "yyyyMMddHHmmss"

$run_id = "run_$current_timestamp"
$eval_id = "eval_$current_timestamp"
$data = "../../../../data/risk-tagging/reviewed_distributed_ddr_v5.csv"

# Execute the pf run create commands
pf run create -f flows/tag_record/batch_run.yaml --name $run_id --data $data
pf run create -f flows/evaluation/batch_run.yaml --run $run_id --name $eval_id --data $data