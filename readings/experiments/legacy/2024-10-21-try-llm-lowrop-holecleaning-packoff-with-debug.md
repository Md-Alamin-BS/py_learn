# Predicting `lowrop`, `holecleaning` and `packoff` issues with an LLM

## Experiment Summary

The goal of this experiment is to evaluate how accurately an LLM (Language Learning Model) can classify a DDR (Daily Drilling Report) with the tags `lowrop`, `holecleaning`, and `packoff`.

### Hypothesis

An LLM can accurately interpret DDR text and determine if it describes a `Lowrop` (Low Rate of Penetration), `Holecleaning`, or `Packoff` scenario.

### Measure of Success

The success of this experiment is measured by the precision, recall, and F1 score on our current evaluation dataset for DDRs.

## Methodology

### Initial Plan

- Focus on classifying using one tag at a time, without predicting multiple tags simultaneously.
- Use the model `gpt-4o-mini` that is [more affordable](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) and faster than `gpt-4o`.
- Provide the LLM with tag definition available on the [InformatiQ Notion](https://informatiq.notion.site/Tag-categories-and-abbreviations-11a0158b598780f2a902d833083c39b5).
- Instruct the LLM to justify its decisions to identify sources of errors, which will enable efficient iteration on prompt engineering and evaluation data correction.
- Also correct the the evaluation data based on Informatiq comments, for example for `lowrop`:
  - Tag as `lowrop` if the rate of penetration is under 10 m/hour.
  - If hard formations and stringers are mentioned, it is very likely to be `lowrop`.
  - If the action describes other actions, like milling, ballooning,  controlled drilling, washing or cleaning the hole, data gathering, logging it shoud **not** be tagged `lowrop`.

### Execution Details

#### Low rate of penetration

Run the `2024-10-21-try-llm-lowrop-with-debug.ipynb` notebook.

Evaluation data was corrected (on the 75% set that was used for training) and the prompt was modified with specific examples.
Performance was tested it on the whole dataset.

#### Hole cleaning

Run the `2024-10-21-try-llm-holecleaning-with-debug.ipynb` notebook.
Similar to the `lowrop` tag, corrected some evaluation data and fine-tuned the prompt with examples.

#### Packoff

Informatiq indicated that this tag is less open to interpretation.
Run the `2024-10-21-try-llm-packoff-with-debug.ipynb` notebook.
The prompt was fine tuned with examples based on coments in evaluation data, evaluation data was not changed.

## Results

We could achieve a higher recall than the current baseline solution for all three tags.

| **Tag**                  | **Precision** | **Recall**  | **F1 Score** |
|--------------------------|---------------|-------------|--------------|
| Baseline **lowrop**      | 0.750000      | 0.718310    | 0.733813     |
| **lowrop**               | 0.780488      | 0.901408    | 0.836601     |
| Baseline **holecleaning**| 0.566038      | 0.833333    | 0.674157     |
| **holecleaning**         | 0.780488      | 0.888889    | 0.831169     |
| Baseline **packoff**     | 0.865169      | 0.950617    | 0.905882     |
| **packoff**              | 0.975904      | 1.0         | 0.987805     |

## Analysis

We observed improvements in both precision and recall compared to the baseline.

### Potential Risks

- Correcting evaluation data with the help of the LLM may introduce bias.
- The prompt might be overfitted to the training data.

## Conclusion

The LLM model can be tuned to recognize instances of `low rate of penetration`, `hole cleaning`, and `packoff` issues. It can also be adjusted to identify that events like logging and simulations should not be tagged. The LLM shows a strong understanding of drilling reports and domain-specific language.

Although these results demonstrate improvements over the existing solution, they cannot be used as a definitive measure of the LLM's capability to predict tags. However, they illustrate that an LLM can enhance the current solution's performance.
