# Experiments

## Overview

This folder contains the framework for local AI experiments.
In particular, it offers a straightforward approach to implementing and evaluating the AI solutions.

## Folder structure

```txt
📁 experiments/
├──📁 1_datasets/              <─── input datasets used in the expeiments. Usually contain ground truth labels.
├──📁 2_assessed_datasets/     <─── you can save an assessed dataset (artifact of the inference stage) in this folder.
├──📁 3_evaluation_results/    <─── you can save the evaluation results (artifact of the evaluation stage) in this folder.
├──📁 common/                  <─── shared Python library that implements common operations. Should be used by the notebooks.
├──📄 .env                     <─── environment variables that will be used by the experiment notebooks.
├──📄 2024-xx-xx-experiment-one.ipynb  <─── notebook for inference/evaluation for experiment #1
├──📄 2024-xx-xx-experiment-one.md     <─── experiment report #1
├──📄 2024-xx-xx-experiment-two.ipynb  <─── notebook for inference/evaluation for experiment #2
└──📄 2024-xx-xx-experiment-two.md     <─── experiment report #2
```

## Datasets

Current datasets:

- **abbreviation_descriptions.csv** - deciphering common abbreviations in the domain of wellbore drlling. [[source](https://informatiq.notion.site/Tag-categories-and-abbreviations-11a0158b598780f2a902d833083c39b5)]
- **reviewed_distributed_ddr.csv** - evaluation dataset for DDRs tagging. Contains DDR texts and the ground truth tags.  [[source](../../spikes/2024-10-15-evaluation-data-for-ddrs/)]
- **reviewed_distributed_events.csv** - evaluation dataset for event tagging. Contains event descriptions, ground truth tags and the extended category of the events. [[source](../../spikes/2024-10-10-get-random-events/)]
- **tag_descriptions.csv** - definitons of the tags used for tagging DDRs and events. Could be used to give LLM more context about the task. [[source](https://informatiq.notion.site/Tag-categories-and-abbreviations-11a0158b598780f2a902d833083c39b5)]

### Updating datasets

To update a dataset, we copy it into a new dataset with a version suffix, e.g. **my_dataset.csv** -> **my_dataset_v2.csv** -> **my_dataset_v3.csv**. This helps quickly understand exactly which dataset was used in a past experiment by reading experiment context.

## Artifacts in the repo

The folders `2_assessed_datasets` and `3_evaluation_results` contain binary Excel files that take ~1-2MiB - experiment artifacts.

We experiment locally and commit these artifacts to the repo, where they forever take space in the Git history.
It's better to be concious of this and **commit only the artifacts that are really needed** to be kept in history, e.g. to support your experiment report.

## Setup

To set up the environment, follow these steps:

1. Create a virtual environment:

    ```sh
    python3 -m venv .venv
    ```

2. Install the required dependencies:

    ```sh
    .venv/bin/pip install -r requirements.txt
    ```

3. Create the `.env` file:

    ```sh
    cp .env.example .env
    ```

4. Edit the `.env` file. Add the environment variables needed for your experiment.

5. When running the notebooks, select this virtual environment (`.venv`) as your Jupyter kernel.

   And if you wish to use the virtual environment in the CLI, you'll need to [activate](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) it each time.
