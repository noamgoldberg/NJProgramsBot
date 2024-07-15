from openai import OpenAI
from typing import Dict, Optional, List
import re
from utils.file_utils import read_file


class LLMAgent:
    def __init__(
        self,
        api_key: str,
        model_name: str = "gpt-3.5-turbo",
        context: str = "",
        query_limit: int = 1000
    ):
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name
        self.context = context
        self.messages: List[Dict[str, str]] = []
        if self.context:
            self.messages += [{"role": "system", "content": self.context}]
        self.query_limit = query_limit
        self.num_queries = 0
        
    def _validate_attr_not_set(self, attr_name: str):
        if hasattr(self, f"_{attr_name}"):
            raise Exception(
                f"Cannot set '{attr_name}' attribute of LLMAgent class instance once it "
                "has already been set"
            )

    def _validate_attr_attr_dtype(self, attr_name, attr_value, dtypes):
        if not isinstance(attr_value, dtypes):
            if not isinstance(dtypes, (list, tuple, set)):
                dtypes = [dtypes]
            raise TypeError(
                f"Invalid type for '{attr_name}' property of LLMAgent class instance; expected "
                f"one of '{[dt.__name__ for dt in dtypes]}', got '{type(attr_value).__name__}'"
            )

    @property
    def context(self) -> str:
        return self._context

    @context.setter
    def context(self, context):
        self._validate_attr_not_set("context")
        self._validate_attr_attr_dtype("context", context, str)
        try:
            self._context = read_file(context)
        except:
            self._context = context
        self.messages = [{"role": "system", "content": self._context}]
    
    def add_messages(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})

    def query(
        self,
        question: str,
        max_tokens: int = 1000,
        temperature: float = 0.7,
        top_p: float = 0.9,
        presence_penalty: float = 1.2,
    ) -> str:
        if self.num_queries >= self.query_limit:
            raise Exception(f"Reached query limit of {self.query_limit} query limits reached")
        self.add_messages("user", question)
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            presence_penalty=presence_penalty,
        )
        self.num_queries += 1
        result = response.choices[0].message.content.strip()
        self.add_messages("assistant", result)
        return result
