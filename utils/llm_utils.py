import os
from typing import Optional

from llm_agent_openai import LLMAgent
from consts import CONTEXT_FILEPATH


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

