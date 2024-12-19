import numpy as np
from promptflow.core import tool, log_metric


@tool
def calculate_average_per_ddr_metrics(
    precisions: list[float], recalls: list[float], f1s: list[float]
) -> dict:

    avg_recall = np.mean(recalls)
    avg_precision = np.mean(precisions)
    avg_f1 = np.mean(f1s)

    log_metric("avg_recall_per_ddr", f"{avg_recall:.3f}")
    log_metric("avg_precision_per_ddr", f"{avg_precision:.3f}")
    log_metric("avg_f1_per_ddr", f"{avg_f1:.3f}")

    return {
        "avg_recall": np.nanmean(recalls),
        "avg_precision": np.nanmean(precisions),
        "avg_f1": np.nanmean(f1s),
    }
