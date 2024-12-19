from typing import Sequence, Set
import pandas as pd
from pydantic import BaseModel


class BaseContext(BaseModel):
    description: str
    experiment_id: str
    run_id: str
    random_seed: int = None

    def as_dataframe(self) -> pd.DataFrame:
        pairs = self.model_dump().items()
        return pd.DataFrame({"key": k, "value": v} for k, v in sorted(pairs))

    def as_dict(self) -> dict:
        return self.model_dump()


class TagPredictionContext(BaseContext):
    tags_in_scope: Sequence | Set
    used_datasets: Sequence | Set = None
    with_notags: bool


class LLMTagPredictionContext(TagPredictionContext):
    llm_system_prompt: str = None
    llm_prompt_template: str = None
    llm_model: str = None
    llm_temperature: float = None
