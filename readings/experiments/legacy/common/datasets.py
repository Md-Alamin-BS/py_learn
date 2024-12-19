import ast
import json
import os
from typing import Tuple
import pandas as pd

from .context import BaseContext
from .evaluation import TagMatchingEvaluator

BASE_FOLDER_NAME_INPUTS = "1_datasets"
BASE_FOLDER_NAME_ASSESSED = "2_assessed_datasets"
BASE_FOLDER_NAME_EVALUATION_RESULTS = "3_evaluation_results"


def load_input_dataset(dataset_name, columns_to_convert_to_sets=()):
    full_dataset_path = os.path.join(BASE_FOLDER_NAME_INPUTS, dataset_name)
    df = _pandas_load(full_dataset_path)

    def convert_value(val: str):
        try:
            return ast.literal_eval(val)
        except Exception as e:
            print("Can't parse:", val, e)
            raise

    for col in columns_to_convert_to_sets:
        df[col] = df[col].apply(
            lambda x: set(convert_value(x)) if pd.notna(x) else set()
        )
    return df


def save_assessed_dataset(
    df: pd.DataFrame, context: BaseContext, experiment_id: str, run_id: str
):
    folder_name = f"{experiment_id}-{run_id}"
    dataset_name = f"{run_id}.xlsx"
    full_dataset_path = os.path.join(
        BASE_FOLDER_NAME_ASSESSED, folder_name, dataset_name
    )
    full_context_path = os.path.join(
        BASE_FOLDER_NAME_ASSESSED, folder_name, "context.json"
    )

    print(os.path.dirname(full_dataset_path))
    os.makedirs(os.path.dirname(full_dataset_path), exist_ok=True)

    with open(full_context_path, "w") as fout:
        json.dump(context.as_dict(), fout, indent=2, sort_keys=True)

    _pandas_save(df, full_dataset_path)


def load_assessed_dataset(experiment_id: str, run_id: str) -> Tuple[pd.DataFrame, dict]:
    folder_name = f"{experiment_id}-{run_id}"
    dataset_name = f"{run_id}.xlsx"
    full_dataset_path = os.path.join(
        BASE_FOLDER_NAME_ASSESSED, folder_name, dataset_name
    )
    full_context_path = os.path.join(
        BASE_FOLDER_NAME_ASSESSED, folder_name, "context.json"
    )

    with open(full_context_path, "r") as fin:
        context = json.load(fin)

    df = _pandas_load(full_dataset_path)

    return df, context


def save_evaluation_report(
    experiment_id: str,
    run_id: str,
    dataset_df: pd.DataFrame,
    assessed_df: pd.DataFrame,
    evaluator: TagMatchingEvaluator,
    context: BaseContext,
):
    folder_name = f"{experiment_id}-{run_id}"
    report_name = f"{run_id}.xlsx"

    report_folder = os.path.join(BASE_FOLDER_NAME_EVALUATION_RESULTS, folder_name)
    os.makedirs(report_folder, exist_ok=True)

    full_report_path = os.path.join(report_folder, report_name)
    eval_metrics_path = os.path.join(report_folder, "eval_metrics.json")
    full_context_path = os.path.join(report_folder, "context.json")

    individual_ddr_evals = evaluator.eval_individual_ddrs()
    per_tag_evaluations = evaluator.eval_per_tag()
    avg_evals_df = evaluator.average_metrics()

    with pd.ExcelWriter(full_report_path, engine="openpyxl") as writer:
        dataset_df.to_excel(writer, sheet_name="Dataset", index=False)
        assessed_df.to_excel(writer, sheet_name="Assessed", index=False)
        individual_ddr_evals.to_excel(writer, sheet_name="Metrics per DDR", index=False)
        per_tag_evaluations.to_excel(writer, sheet_name="Metrics per tag", index=False)
        avg_evals_df.to_excel(writer, sheet_name="Average metrics", index=False)
        context.as_dataframe().to_excel(writer, sheet_name="Run Context", index=False)

        beautify_excel_book(writer)

    with open(eval_metrics_path, "w") as fout:
        json.dump(
            {
                "averages": avg_evals_df.to_dict("records"),
                "per_tag": per_tag_evaluations.to_dict("records"),
            },
            fout,
            indent=2,
        )

    with open(full_context_path, "w") as fout:
        json.dump(context.as_dict(), fout, indent=2)


def beautify_excel_book(writer: pd.ExcelWriter):
    """
    Make columns wider, add filters to the columns.
    """
    for sheet_name in writer.sheets:
        worksheet = writer.sheets[sheet_name]
        for col in worksheet.columns:
            max_length = min(20, max(len(str(cell.value)) for cell in col))
            worksheet.column_dimensions[col[0].column_letter].width = max_length

        # Add filters to all columns
        worksheet.auto_filter.ref = worksheet.dimensions


def _pandas_save(df: pd.DataFrame, full_path: str):
    if full_path.endswith(".csv"):
        df.to_csv(full_path)
    elif full_path.endswith(".jsonl"):
        df.to_json(full_path, orient="records", lines=True)
    elif full_path.endswith(".json"):
        df.to_json(full_path, orient="records", lines=False)
    elif full_path.endswith(".xlsx"):
        df.to_excel(full_path, index=False)
    else:
        raise ValueError(f"Unsupported file extension for dataset: {full_path}")


def _pandas_load(full_path: str) -> pd.DataFrame:
    if full_path.endswith(".csv"):
        return pd.read_csv(full_path)
    elif full_path.endswith(".jsonl"):
        return pd.read_json(full_path, orient="records", lines=True)
    elif full_path.endswith(".json"):
        return pd.read_json(full_path, orient="records", lines=False)
    elif full_path.endswith(".xlsx"):
        return pd.read_excel(full_path, index=False)
    else:
        raise ValueError(f"Unsupported file extension for dataset: {full_path}")
