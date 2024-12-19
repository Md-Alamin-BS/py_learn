import unittest
from unittest.mock import patch
from flows.tag_record.parse_output import parse_output
import json


class TestParseOutput(unittest.TestCase):

    def test_valid_input(self):
        llm_response = json.dumps(
            {
                "response": [
                    {
                        "risk": "tighthole",
                        "applies": "yes",
                        "justification": "The use of lubrication suggests potential tighthole issues, as it indicates difficulties in running tools or casing due to reduced wellbore diameter.",
                    },
                    {
                        "risk": "surfeqfailure",
                        "applies": "no",
                        "justification": "Not relevant in this context.",
                    },
                ]
            }
        )

        expected_output = {
            "tags_with_justification": [
                {
                    "tag": "tighthole",
                    "present": True,
                    "justification": "The use of lubrication suggests potential tighthole issues, as it indicates difficulties in running tools or casing due to reduced wellbore diameter.",
                },
                {
                    "tag": "surfeqfailure",
                    "present": False,
                    "justification": "Not relevant in this context.",
                },
            ],
            "assigned_tags": ["tighthole"],
        }

        result = parse_output(llm_response)
        self.assertEqual(result, expected_output)

    def test_empty_response(self):
        llm_response = json.dumps({"response": []})
        expected_output = {"tags_with_justification": [], "assigned_tags": []}

        result = parse_output(llm_response)
        self.assertEqual(result, expected_output)

    def test_partial_fields(self):
        llm_response = json.dumps(
            {
                "response": [
                    {"risk": "tighthole"},
                    {"applies": "yes"},
                    {"justification": "No risk."},
                ]
            }
        )

        expected_output = {
            "tags_with_justification": [
                {"tag": "tighthole", "present": False, "justification": ""},
                {"tag": "unknown", "present": True, "justification": ""},
                {"tag": "unknown", "present": False, "justification": "No risk."},
            ],
            "assigned_tags": ["unknown"],
        }

        result = parse_output(llm_response)
        self.assertEqual(result, expected_output)

    def test_debug_logging(self):
        llm_response = json.dumps(
            {
                "response": [
                    {
                        "risk": "packoff",
                        "applies": "yes",
                        "justification": "Test justification.",
                    }
                ]
            }
        )

        with patch("builtins.print") as mock_print:
            parse_output(llm_response, debug=True)

            mock_print.assert_any_call(" Risk packoff applies yes, bool True")
            mock_print.assert_any_call(
                "********************************************************"
            )
            mock_print.assert_any_call(
                "Risk: packoff - Present: True - Justification: Test justification."
            )

    @patch("logging.Logger.error")
    def test_invalid_json_input(self, mock_logger_error):
        invalid_json = "this is not valid json"
        with self.assertRaises(ValueError):
            parse_output(invalid_json)

        mock_logger_error.assert_called_once_with("Invalid JSON input")


if __name__ == "__main__":
    unittest.main()
