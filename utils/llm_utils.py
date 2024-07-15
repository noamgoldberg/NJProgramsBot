import os
from typing import Optional

from llm_agent_openai import LLMAgent
from utils.hash_utils import hash_str
from consts import CONTEXT_FILEPATH, OPENAI_API_KEY_HASH


def is_openai_api_key_valid(openai_api_key: str) -> bool:
    return hash_str(openai_api_key) == OPENAI_API_KEY_HASH

def initialize_llm(
    openai_api_key: Optional[str] = None,
    model_name: str = "gpt-3.5-turbo",
    use_context: bool = True,
    query_limit: int = 1000,
):
    return LLMAgent(
        api_key=openai_api_key or os.environ["OPENAI_API_KEY"],
        model_name=model_name,
        context=CONTEXT_FILEPATH if use_context else "",
        query_limit=query_limit
    )

