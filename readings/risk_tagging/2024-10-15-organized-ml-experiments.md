# Organized ML experiments

## Overview

We aim to conduct many experiments on DDR tagging and preserve the results for future analysis.

This ADR proposes how to organize such experiments.

## Decisions

- Conduct experiments using local Jupyter notebooks and commit the results as files to the repository.
- Ensure experiment results include comprehensive context, such as model parameters, hyperparameters, LLM prompts, input data, etc., to facilitate reproducibility.
- Develop a common library for the evaluation pipeline that can be imported in the notebooks, ensuring consistent result formats and uniform evaluation metrics across experiments. Evaluation metrics for the classification should inclide precision, recall and the f1-score. These can be calculated per tag or per DDR, and also should be averaged over the dataset.
- Separate the stages of applying the model to the data and evaluating the results.
- Use a common markdown template for documenting experiments. This template should outline the hypothesis and test approach before the experiment and include result analysis (if necessary, error analysis) afterwards. See example template [here](../../.attachments/example_experiment_template.md).

## Rationale

Using local Jupyter notebooks leverages familiar tools like Jupyter and Git. We can consider transitioning to a cloud solution (e.g. Azure Machine Learning) in the future.

Adopting a uniform format for experiment descriptions and results is a known best practice. It ensures experiments have clear objectives and their artifacts are valuable for future analysis.

Separating the stages of applying the model and evaluating the results helps in case applying the model
is slow and/or expensive (e.g. calling an LLM), and we want to reevaluate the results.
