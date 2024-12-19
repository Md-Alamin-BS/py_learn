from functools import cache
from typing import Iterable
import pandas as pd
from sklearn.metrics import f1_score, precision_score, recall_score


class TagMatchingEvaluator:
    def __init__(
        self,
        *,
        assessed_df: pd.DataFrame,
        tags_in_scope: Iterable,
        with_notags,
        ground_truth_tag_prefix="expected",
        predicted_tag_prefix="actual",
    ) -> None:
        """
        Initializes the evaluator class with the provided parameters.
        Args:
            assessed_df (pd.DataFrame): The DataFrame containing the assessed data. Should have 2 binary columns for each tag in scope: predicted and ground truth values.
            tags_in_scope (Iterable): Tags that are within the scope of the evaluation.
            with_notags (bool): A flag indicating whether to create artificial "notag" tag for calculating precision/recall per DDR. This helps to avoid the 0/0 situation for the DDRs with no tags.
            ground_truth_tag_prefix (str, optional): The column name prefix used for ground truth tag values.
            predicted_tag_prefix (str, optional): The column name prefix used for predicted tag values.
        """
        self.df = assessed_df
        self.tags_in_scope = tags_in_scope
        self.ground_truth_tag_prefix = ground_truth_tag_prefix
        self.predicted_tag_prefix = predicted_tag_prefix
        self.with_notags = with_notags

    @cache
    def eval_individual_ddrs(self):
        return evaluate_individual_ddrs(
            df=self.df,
            tags_in_scope=self.tags_in_scope,
            ground_truth_tag_prefix=self.ground_truth_tag_prefix,
            predicted_tag_prefix=self.predicted_tag_prefix,
            with_notags=self.with_notags,
        )

    @cache
    def eval_per_tag(self):
        return evaluate_per_tag(
            df=self.df,
            tags_in_scope=self.tags_in_scope,
            ground_truth_tag_prefix=self.ground_truth_tag_prefix,
            predicted_tag_prefix=self.predicted_tag_prefix,
        )

    @cache
    def average_metrics(self):
        micro = (
            self.eval_individual_ddrs()[["precision", "recall", "f1"]]
            .mean()
            .to_frame()
            .T
        )
        macro = self.eval_per_tag()[["precision", "recall", "f1"]].mean().to_frame().T
        micro.insert(loc=0, column="Type", value="Average per DDR")
        macro.insert(loc=0, column="Type", value="Average per Tag")
        return pd.concat([micro, macro], ignore_index=True)


def evaluate_individual_ddrs(
    df: pd.DataFrame,
    tags_in_scope: Iterable,
    ground_truth_tag_prefix="expected",
    predicted_tag_prefix="actual",
    with_notags=True,
):
    tags_in_scope = sorted(tags_in_scope)
    df_with_metrics = df.copy()

    if with_notags:
        notags_tag_name = "notags"
        df_with_metrics[f"{ground_truth_tag_prefix}__{notags_tag_name}"] = (
            df_with_metrics.apply(
                lambda row: not any(
                    row[f"{ground_truth_tag_prefix}__{tag}"] for tag in tags_in_scope
                ),
                axis=1,
            )
        )
        df_with_metrics[f"{predicted_tag_prefix}__{notags_tag_name}"] = (
            df_with_metrics.apply(
                lambda row: not any(
                    row[f"{predicted_tag_prefix}__{tag}"] for tag in tags_in_scope
                ),
                axis=1,
            )
        )
        tags_in_scope += [notags_tag_name]

    def ground_truth(row):
        return [row[f"{ground_truth_tag_prefix}__{tag}"] for tag in tags_in_scope]

    def predicted(row):
        return [row[f"{predicted_tag_prefix}__{tag}"] for tag in tags_in_scope]

    df_with_metrics["precision"] = df_with_metrics.apply(
        lambda row: precision_score(ground_truth(row), predicted(row), zero_division=1),
        axis=1,
    )
    df_with_metrics["recall"] = df_with_metrics.apply(
        lambda row: recall_score(ground_truth(row), predicted(row), zero_division=1),
        axis=1,
    )
    df_with_metrics["f1"] = df_with_metrics.apply(
        lambda row: f1_score(ground_truth(row), predicted(row), zero_division=1),
        axis=1,
    )
    df_with_metrics["true_positives"] = df_with_metrics.apply(
        lambda row: true_positives(ground_truth(row), predicted(row)),
        axis=1,
    )
    return df_with_metrics


def evaluate_per_tag(
    df: pd.DataFrame,
    tags_in_scope: Iterable,
    ground_truth_tag_prefix="expected",
    predicted_tag_prefix="actual",
) -> pd.DataFrame:
    evaluation_results = []

    for tag in tags_in_scope:
        ground_truth = df[f"{ground_truth_tag_prefix}__{tag}"]
        predicted = df[f"{predicted_tag_prefix}__{tag}"]

        precision = precision_score(ground_truth, predicted, zero_division=1)
        recall = recall_score(ground_truth, predicted, zero_division=1)
        f1 = f1_score(ground_truth, predicted, zero_division=1)
        tp = true_positives(ground_truth, predicted)
        positive_examples = sum(ground_truth)
        negative_examples = len(ground_truth) - positive_examples

        evaluation_results.append(
            {
                "tag": tag,
                "precision": precision,
                "recall": recall,
                "f1": f1,
                "true_positives": tp,
                "positives_in_ground_truth": positive_examples,
                "negatives_in_ground_truth": negative_examples,
            }
        )

    eval_df = pd.DataFrame(evaluation_results)
    eval_df = eval_df.sort_values(by="tag")
    return eval_df


def true_positives(ground_truth: Iterable[bool], predicted: Iterable[bool]):
    return sum(1 for a, b in zip(ground_truth, predicted) if a and b)
