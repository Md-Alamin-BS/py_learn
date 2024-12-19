import logging
import string

from promptflow.core import tool

logger = logging.getLogger(__name__)

TAG = "tighthole"
NOTAG = "notag"


@tool
def parse_output(llm_response: str) -> str:
    def normalize_tag(t):
        # sometimes the model returns extra text like "1. tighthole" or "tags: tighthole"
        t = t.lower()
        if TAG in t:
            return TAG
        if NOTAG in t:
            return NOTAG

        print("Unexpected tag:", t)
        return t

    response = llm_response.strip().strip(string.punctuation)
    if "\n" in response:
        justification, tag = response.strip().rsplit("\n", 1)
    else:
        justification, tag = response.strip().rsplit(None, 1)

    tag = normalize_tag(tag)
    justification = justification.strip()

    return [{"tag": TAG, "present": tag == TAG, "justification": justification}]
