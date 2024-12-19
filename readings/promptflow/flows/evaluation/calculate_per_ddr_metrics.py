from promptflow.core import tool
from sklearn.metrics import f1_score, precision_score, recall_score
from common import parse_set


@tool
def calculate_per_ddr_metrics(prediction: list[dict], groundtruth: str) -> dict:
    tags_in_scope = {tag["tag"] for tag in prediction}
    predicted_tags = {tag["tag"] for tag in prediction if tag["present"]}
    groundtruth_tags = parse_set(groundtruth) & tags_in_scope

    prediction_matches = [tag in predicted_tags for tag in tags_in_scope]
    prediction_matches.append(
        not predicted_tags
    )  # artificial tag that says "no tags" to avoid division by zero

    groundtruth_matches = [tag in groundtruth_tags for tag in tags_in_scope]
    groundtruth_matches.append(
        not groundtruth_tags
    )  # artificial tag that says "no tags" to avoid division by zero

    return {
        "precision": precision_score(
            groundtruth_matches, prediction_matches, zero_division=1
        ),
        "recall": recall_score(
            groundtruth_matches, prediction_matches, zero_division=1
        ),
        "f1": f1_score(groundtruth_matches, prediction_matches, zero_division=1),
    }
