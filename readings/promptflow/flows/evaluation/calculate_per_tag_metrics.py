import numpy as np
from promptflow.core import tool, log_metric
from sklearn.metrics import f1_score, precision_score, recall_score
from common import parse_set


@tool
def calculate_metrics(predictions: list[list[dict]], groundtruths: list[str]) -> dict:
    """
    For every assessed tag, calculate precision and recall on the full dataset.
    """
    tags_in_scope = {tag["tag"] for tags in predictions for tag in tags}

    tag_predictions = [
        {tag["tag"] for tag in tags if tag["present"]} for tags in predictions
    ]
    tag_groundtruths = [parse_set(x) for x in groundtruths]

    results = {}

    for tag in sorted(tags_in_scope):
        groundtruth_matches = [tag in tags for tags in tag_groundtruths]
        prediction_matches = [tag in tags for tags in tag_predictions]

        results[tag] = {
            "precision": precision_score(
                groundtruth_matches, prediction_matches, zero_division=1
            ),
            "recall": recall_score(
                groundtruth_matches, prediction_matches, zero_division=1
            ),
            "f1": f1_score(groundtruth_matches, prediction_matches, zero_division=1),
        }
        log_metric(f"{tag} precision", f"{results[tag]['precision']:.3f}")
        log_metric(f"{tag} recall", f"{results[tag]['recall']:.3f}")
        log_metric(f"{tag} f1", f"{results[tag]['f1']:.3f}")

    avg_recall = np.nanmean([x["recall"] for x in results.values()])
    avg_precision = np.nanmean([x["precision"] for x in results.values()])
    avg_f1 = np.nanmean([x["f1"] for x in results.values()])

    log_metric("avg_recall_per_tag", f"{avg_recall:.3f}")
    log_metric("avg_precision_per_tag", f"{avg_precision:.3f}")
    log_metric("avg_f1_per_tag", f"{avg_f1:.3f}")

    return {
        "avg_recall": avg_recall,
        "avg_precision": avg_precision,
        "avg_f1": avg_f1,
        "all_metrics": results,
    }
