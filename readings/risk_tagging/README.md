# Risk Assistant Datasets

Collection of datasests related to the risk assistant.
The main dataset used for evaluation is `reviewed_distributed_ddr_v5.csv` The
dataset was created by:

1. Taking 300 DDRs from this split: 150 from DDRs with some tags assigned by
   the regex algorithm, and 150 that had no tag assigned.
1. SMEs reviewed DDRs and assigned tags. No tag suggestion was shown to the
   SMEs to avoid introducing bias in labeling.

Data was extracted with a [Python notebook](../../spikes/2024-11-05-get-random-ddrs/extract_ddrs_for_evaluation.ipynb)
and sent to curation with the following columns:

- id
- comment
- phase
- code
- subCode
- is_shallowwater
- comment_to_shallowwater
...
- is_wait
- comment_to_wait

Tags were removed to eliminate bias and each tag was mentioned to make sure none is missed.

Then the format was changed back to the format that our evaluation pipelines use using
[another Python notebook](../../spikes/2024-11-05-get-random-ddrs/change_format.ipynb).

These are the current required columns for Daily Drilling Reports:

- id
- text
- phase
- code
- subCode
- tags
- reviewedTags

If required, a baseline for this evaluation data can be calculated using [this Python notebook](../../experiments/legacy/2024-10-16-baseline-data-ddrs.ipynb).

## Updating the evaluation data

To add/update the evaluation data:

- create a new file with an incremented version number
- update the `batch_run.yaml` files of the flows: `data` and, if relevant, `column_mapping`
- calculate LLM performance metrics on the new dataset by triggering the promptflow run either
 [from the local machine](../../src/promptflow/README.md) or from the [evaluation pipeline](../../build/pipelines/risk-tagging-continuous-evaluation.yaml)
- (optional) calculate the baseline (regex) performance on the new dataset by updating [the baseline notebook](../../experiments/legacy/2024-10-16-baseline-data-ddrs.ipynb)
