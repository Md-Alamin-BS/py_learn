import logging
import json

from promptflow.core import tool

logger = logging.getLogger(__name__)


@tool
def parse_output(llm_response: str, debug=False):
    # Parse JSON string input
    try:
        parsed_data = json.loads(llm_response)
    except json.JSONDecodeError as exc:
        logger.error("Invalid JSON input")
        raise ValueError("LLM response is not valid JSON") from exc

    # Process each risk in the list
    results = []
    assigned_tags = []
    for risk_item in parsed_data["response"]:
        # Extract each field and ensure 'present' is explicitly set as True if "yes" is found
        risk = risk_item.get("risk", "unknown").strip()
        applies_field = risk_item.get("applies", "").strip().lower()
        applies = (
            "yes" in applies_field
        )  # True if "yes" is anywhere in the applies field
        if debug:
            print(f" Risk {risk} applies {applies_field}, bool {applies}")

        justification = risk_item.get("justification", "").strip()

        # Append each risk result in the expected format
        results.append(
            {
                "tag": risk,  # Use risk name directly as the tag
                "present": applies,  # "True" if "yes" found, otherwise False
                "justification": justification,
            }
        )
        if applies:
            assigned_tags.append(risk)

    # Logging results for verification
    if debug:
        for result in results:
            print("********************************************************")
            print(
                f"Risk: {result['tag']} - Present: {result['present']} - Justification: {result['justification']}"
            )

    return {
        "tags_with_justification": results,
        "assigned_tags": assigned_tags,
    }
