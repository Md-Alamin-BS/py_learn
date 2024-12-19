from typing import Iterable
import pandas as pd


def expand_ext_categories(
    df: pd.DataFrame,
    categories_in_scope: Iterable,
    ground_truth_column="extendedCategory",
    predicted_column="predictedExtendedCategory",
    ground_truth_tag_prefix="expected",
    predicted_tag_prefix="actual",
):
    """
    Replace columns that contain extendedCategories (ground truth and predicted) by 2 boolean columns per category type.
    """
    categories_in_scope = sorted(set(categories_in_scope))

    df = df.copy()

    for tag in categories_in_scope:
        df[f"{ground_truth_tag_prefix}__{tag}"] = df[ground_truth_column].apply(
            lambda x: tag == x
        )
        df[f"{predicted_tag_prefix}__{tag}"] = df[predicted_column].apply(
            lambda x: tag == x
        )

    return df


def expand_tags(
    df: pd.DataFrame,
    tags_in_scope: Iterable,
    ground_truth_tags_column="Reviewed tags",
    predicted_tags_column="tags",
    ground_truth_tag_prefix="expected",
    predicted_tag_prefix="actual",
):
    """
    Replace columns that contain lists of tags (ground truth and predicted) by 2 boolean columns per tag.
    """
    tags_in_scope = sorted(set(tags_in_scope))

    df = df.copy()

    for tag in tags_in_scope:
        df[f"{ground_truth_tag_prefix}__{tag}"] = df[ground_truth_tags_column].apply(
            lambda x: tag in x
        )
        df[f"{predicted_tag_prefix}__{tag}"] = df[predicted_tags_column].apply(
            lambda x: tag in x
        )

    return df.drop(columns=[ground_truth_tags_column, predicted_tags_column])
