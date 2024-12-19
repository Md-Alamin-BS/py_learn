# Continuous Improvement of Risk Tagging Model

## Context

As a user/developer of the risk tagging model, it is important to continuously monitor its performance to ensure it remains effective with new examples. If LLM generated tags start being challenged consistently, it indicates a potential issue with the model that needs immediate attention.

## Decision

Implement a continuous improvement process for the risk tagging model to monitor its performance and address any discrepancies between tags suggested by the LLM and the tags reviewed by subject matter experts (SMEs).

## Suggestions for the continuous improvement process

Following measures must be taken to ensure model remains accurate and reliable.

1. Performance Monitoring

    Implement automated monitoring to compare LLM suggested tags with tags reviewed by SMEs. Alerts should be triggered if the differences exceed a predefined threshold.

1. Feedback Loop

    The updated UI will allow users to report any inconsistencies they observe. This feedback should be used to engineer the system prompt and improve the model using the [experiment process](../../../docs/experimentation-process.md).

1. Regular Updates of the Evaluation Data

    The model is evaluated [continuously using a pipeline](../../../build/pipelines/risk-tagging-continuous-evaluation.yaml). Regularly review and update the evaluation data by adding new examples. This ensures the evaluation remains accurate, even if the daily drilling reports adopt a new writing style. Remove any data from the evaluation set used during prompt engineering.
