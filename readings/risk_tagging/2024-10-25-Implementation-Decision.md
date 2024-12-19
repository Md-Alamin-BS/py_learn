# Module Implementation Decision

## Decision

We have decided to:

- utilize GPT with customized prompts for the tagging module;
- use Azure OpenAI Studio for managing LLMs;
- use Azure Machine Learning for managing prompts and experiments.

## Context

We need a robust and scalable solution for managing large language models (LLMs), prompts, and experiments. Additionally, we require an efficient tagging module that can be implemented quickly without extensive data preparation.

## Rationale

### Azure OpenAI Studio and Azure Machine Learning

- **Enterprise Grade Offering**:
  - Provides a robust platform for managing LLMs, prompts, and experiments, ensuring compliance with enterprise security and compliance standards.
  - **Mature Microsoft Support Model**:
    - **Direct Contact with Product Groups (PGs)**: Customers facing critical issues or blockers can engage directly with the Azure AI PGs, including Azure ML, Prompt Flow, Azure OpenAI, Azure AI Studio, and Azure AI Search.
    - **Azure Support Requests**: Customers can create and manage support requests for Azure AI services through the Azure portal.
    - **Community Support**: Customers can get quick and reliable answers to their technical questions from Microsoft Engineers, Azure MVPs, or the expert community on Microsoft Q&A and Stack Overflow.
- **Scalability and Flexibility**:
  - **Variety of Models**: Access to a wide range of powerful language models.
  - **Flexible Access**: Programmatic access via REST APIs, Python SDK, or web interface.
  - **Data Compliance**: Secure environment for handling sensitive data.
  - **Fine-Tuning Support**: Ability to fine-tune models for specific needs.
  - **Scalability**: Designed to handle large-scale deployments.
  - **Integration**: Seamless integration with other Azure services.
  - **User-Friendly**: Easy-to-use web-based interface.
  - **Monitoring and Feedback**: Features for ongoing performance monitoring and feedback.

### GPT with Customized Prompts for Tagging

Using prompts with GPT for tagging is a strategic choice that enables us to quickly implement a solution for the tagging module.

- **Immediate Usability**: Prompts can be used right away without extensive data preparation.
- **Observed Improvements**: During experimentation and investigations, we have observed that the LLM is already performing better than the existing solution.
- **Adaptability**: The current regex solution is optimized for the existing dataset, whereas an LLM solution, which can understand context, would be beneficial for handling new and unfamiliar datasets.
- **Flexibility**: Easily adjustable prompts to meet specific tagging needs.
- **Cost-Effective**: More affordable in the short term compared to fine-tuning.
- **Scalability**: Suitable for large-scale data and complex queries.
- **Future Fine-Tuning**: Although there is not enough data to fine-tune a model at this time, there is the potential to fine-tune the model as more data becomes available.
- **Performance Monitoring**: Allows for continuous monitoring and iterative improvements.

### Comparison between existing solution and a Large Language Model

We wanted to compare the performance of the current solution to a large language model.

Used Metrics:

- **Precision**: How often the tag was correct when predicted.
- **Recall**: How well the model identifies all relevant cases of the tag.
- **F1 Score**: The harmonic mean of precision and recall, balancing both.
- **True Positives**: The number of correct predictions for the tag.
- **Positives in Ground Truth**: The actual number of cases where the tag should have been applied.
- **Negatives in Ground Truth**: The number of cases where the tag should not have been applied.

To speed the process, we chose three tags:

- `lowrop`, as it has a high number of occurances and a more problematic definition
- `holecleaning`, chosen randomly
- `packoff`, as it was indicated to be a tag that is less open to interpretation

#### Existing solution

The existing solution uses [rules](../../.attachments/tag-ruleset.json) to determine tags based on keywords and skip words found in certain fields (`Phase`, `Operation.SubCode`, `Comment`) for Drilling Reports.

| **Tag**         | **Precision** | **Recall**  | **F1 Score** | **True Positives** | **Positives in Ground Truth** | **Negatives in Ground Truth** |
|-----------------|---------------|-------------|--------------|--------------------|------------------------------|--------------------------------|
| **lowrop**      | 0.750000      | 0.718310    | 0.733813     | 102                | 142                          | 1300                           |
| **holecleaning**| 0.566038      | 0.833333    | 0.674157     | 30                 | 36                           | 1406                           |
| **packoff**     | 0.865169      | 0.950617    | 0.905882     | 77                 | 81                           | 1361                           |

### Large Language Model (LLM)

[Experiments with a LLM were conducted](https://dev.azure.com/informatiq/AkerBP%20AI/_git/AkerBP%20AI/pullrequest/17) and we were able to write prompts that show we can improve recall and precision of the existing tagging solution.

| **Tag**         | **Precision** | **Recall**  | **F1 Score** | **True Positives** | **Positives in Ground Truth** | **Negatives in Ground Truth** |
|-----------------|---------------|-------------|--------------|--------------------|------------------------------|--------------------------------|
| **lowrop**      | 0.780488      | 0.901408    | 0.836601     | 128                | 142                          | 1300                           |
| **holecleaning**| 0.780488      | 0.888889    | 0.831169     | 32                 | 36                           | 1406                           |
| **packoff**     | 0.975904      | 1.0         | 0.987805     | 81                 | 81                           | 1361                           |

#### Shortcomings for the experiments

- Prompts are tailored to the specific dataset, and maybe made too specific, no evaluation set was used to verify these numbers.
- Evaluation data was reviewed following hints from LLM. This may introduce a bias and data should be reviewed again (this is in progress).
- Tests were conducted with only three tags, other tags may prove to be more challenging.

### Consequences

- **Pros**:
  - Quick implementation and immediate usability of the tagging module.
  - Flexibility and scalability in managing LLMs and prompts.
  - Secure and compliant environment for data handling.
  - Potential for future fine-tuning as more data becomes available.
- **Cons**:
  - Relying initially on prompts with a large language model (LLM) may not achieve the same level of accuracy as using a finely tuned model.
  - Future effort required for fine-tuning the model as more data becomes available.
