import logging
from openai import OpenAI
from pydantic import BaseModel, Field
from termcolor import colored
import os

logging.basicConfig(level=logging.INFO)

default_suggestions = os.getenv("SHAI_DEFAULT_SUGGESTIONS", 2)


class CommandSuggestion(BaseModel):
    """Details of a command suggestion."""

    commands: list[str] = Field(description="Valid command-line commands")


class LLMClient:
    def __init__(self, api_key: str, base_url: str, model_name: str):
        self.model_name = model_name
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def get_command_suggestions(self, user_command: str) -> list[str]:
        logging.info(
            colored(
                f"Getting command suggestions for: {user_command}, model: {self.model_name} ...",
                "yellow",
            )
        )
        response = self.client.beta.chat.completions.parse(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that suggests valid command-line commands based on user's intent.",
                },
                {
                    "role": "user",
                    "content": f"Suggest a list of valid command-line commands related to: '{user_command}'.  Return just a plain list of commands, one command per line, no explanations or extra text.  Keep the list concise (max {default_suggestions} commands)",
                },
            ],
            response_format=CommandSuggestion,
        )
        if response.choices[0].message.parsed:
            return response.choices[0].message.parsed.commands
        else:
            raise ValueError(colored("No valid command suggestions found.", "red"))
