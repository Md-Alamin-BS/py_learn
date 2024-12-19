# How to Set Up AML Dashboard

## Introduction

This guide will show you how to set up an [Azure Machine Learning dashboard](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-visualize-jobs?view=azureml-api-2)
to visualize the metrics of past evaluation jobs.

This helps you to track the history of the offline evaluations and compare their metrics.

At the moment, these Dashboards can not be created programmatically and require manual setup. Fortunately, the setup is simple.

## Step-by-Step Guide

### 1. Navigate to the  AML workspace

1. Sign in to the [*Azure portal*](https://portal.azure.com).
2. Open the Azure Machine Learning workspace, launch the Machine Learning Studio. You should be redirected to [ml.azure.com](https://ml.azure.com).

### 2. Open the Job

All prompt flow runs that run on AML implicitly belong to a Job.

In case of the evaluation runs for Risk Tagging, the job is called "evaluation" - see [the corresponding flow id](../../src/promptflow/flows/evaluation/flow.dag.yaml). Navigate to this job.

![Job view](../.attachments/aml-dashboard-1.png)

### 3. Create a View

When you open the job, you will see a list of all runs associated with this job on the left side of the screen. On the right side, you will find the default dashboards, one dashboards for each metric that was logged by this job.

Now select only the runs that you want to visualize.

In case of the evaluation runs for Risk Tagging, you can filter by the prompt flow runs by their **Tags**:

- **branch**: main
- **purpose**: continuous_evaluation
- **service**: risk-tagging

![Filter button](../.attachments/aml-dashboard-2.png)
![Filters](../.attachments/aml-dashboard-3.png)

The dashboards on the right will automatically update to show the metrics of the selected runs. They will show the history of each metric across the runs.

You can search for the metrics of interest like this:

![Metric filter](../.attachments/aml-dashboard-6.png)

Now save the view:

![Save as new view button](../.attachments/aml-dashboard-4.png)
![Save dialog](../.attachments/aml-dashboard-5.png)

### 4. Keep the view updated

When you eventually create more runs that match the filter criteria, they will be added to the list of runs for your view as invisible and won't be displayed on the dashboard by default.

You can manually mark them as visible by clicking on the eye icon next to the run. Then save the updated view.

![Mark visible](../.attachments/aml-dashboard-7.png)
![Save view](../.attachments/aml-dashboard-8.png)
