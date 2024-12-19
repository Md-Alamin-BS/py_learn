# Predicting `extendedCategory` of the events with an LLM

## Experiment Summary

Goal of the experiment is to see how accurately an LLM can classify a drilling event
into a specific **extended category**. Although this is not in scope for the current activity, it's interesting to see how well the LLM can do it.

All drilling events belong to a single extended category that is supposed to most accurately explain the event.
Our evaluation dataset contains events from the following 12 extended categories:

```json
[
    "boulders",
    "harddrilling",
    "holecleaning",
    "lostcirculation",
    "other",
    "packoff",
    "shallowgas",
    "stuck",
    "tighthole",
    "waterflow",
    "wellborestability",
    "wellcontrol",
]
```

### Hypothesis

LLM can grasp the meaning of the event description and classify its extended category
well enough given only the examples (multi-shot prompting).

### Measure of Success

Precision/recall/F1 (average for all categories) on the current evaluation dataset - `reviewed_distributed_events.csv`.

## Methodology

### Initial Plan

- Have single prompt that asks LLM to pick an extended category from the list.
- Ask LLM to justify its decision in order to know why it makes mistakes and efficiently iterate on prompt engineering.
- Give LLM examples for each category from the dataset. Remove these examples from the eval dataset.
- Use the model `gpt-4o-mini`.

### Execution Details

Run the `2024-10-24-try-llm-for-extended-category.ipynb` notebook with different `RUN_ID`-s.

Experimented with the prompt:

- Give 1 or 2 examples per extended category.
- Try different random seeds for selecting the examples (poor man's cross-validation).

## Results

### Giving 1 example

| Random Seed | Precision | Recall   | F1 Score |
|-------------|-----------|----------|----------|
| 42          | 0.706029  | 0.803976 | 0.721349 |
| 43          | 0.663547  | 0.691564 | 0.618808 |
| 44          | 0.690455  | 0.755498 | 0.680320 |
| 45          | 0.674149  | 0.719571 | 0.632745 |
| _average_   | 0.68      | 0.74     | 0.66     |

### Giving 2 examples

| Random Seed | Precision | Recall   | F1 Score |
|-------------|-----------|----------|----------|
| 42          | 0.695764  | 0.741545 | 0.656431 |
| 43          | 0.691054  | 0.707113 | 0.649094 |
| 44          | 0.654920  | 0.676408 | 0.626505 |
| 45          | 0.687833  | 0.696185 | 0.652298 |
| _average_   | 0.68      | 0.71     | 0.65     |

## Analysis

Brief error analysis shows many records that have ambiguous or likely incorrect ground truth extended categories, for instance:

```text
Excessive cuttings while circulating after running casing.         Category: Hydraulics, Subcategory: Poor hole cleaning

Ground truth:  "other"
Predicted:     "holecleaning"
Justification: The event indicates issues with maintaining a clean hole due to excessive cuttings, which aligns with the hole cleaning category.
```

```text
Torque and Vibration drilling Glacial Boulders.  Overpull observed and balling of stabs in soft sediments.         Category: Mechanical, Subcategory: Excessive torque

Ground truth:  "harddrilling"
Predicted:     "boulders"
Justification: The event involves drilling through glacial boulders, which is causing torque and vibration issues. This aligns with the challenges associated with boulders in drilling operations.
```

In other cases, LLM makes surprisingly silly mistakes:

```text
Pack off and losses

Ground truth:  "packoff"
Predicted:     "wellborestability"
Justification: The event indicates a situation where the wellbore is obstructed, leading to a pack-off and associated losses. This aligns with issues related to wellbore stability.
```

## Conclusion

Multi-shot prompting with random examples gets average recall and precision to around **~0.7**
on the current evaluation dataset.

This is partially due to the ambiguity of the existing extended categories on the events.
In many cases, multiple extended categories seem to match the event.

Another likely cause of the subpar performance is that the tested prompt was very generic.
It contained examples, but it didn't explain the meaning of the extended categories.
