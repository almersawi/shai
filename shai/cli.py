import click
import inquirer
import subprocess
import logging
from termcolor import colored
import os

from shai.llm_client import LLMClient


# --- Configuration ---

MODEL_NAME = os.getenv("SHAI_MODEL_NAME")
BASE_URL = os.getenv("SHAI_BASE_URL")
API_KEY = os.getenv("SHAI_API_KEY")


def interactive_command_selection(commands):
    """Uses inquirer to let the user interactively select a command."""
    if not commands:
        logging.info(colored("No commands suggested.", "yellow"))
        return None

    questions = [
        inquirer.List(
            "command",
            message="Choose a command to execute:",
            choices=commands,
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers:
        return answers["command"]
    return None


@click.command()
@click.argument(
    "user_command_input", nargs=-1
)  # Allow capturing all parts of the command
def cli(user_command_input):
    """
    CLI tool to get command suggestions from OpenAI and interactively select one.
    Example: tool-name list active docker containers
    """
    llm_client = LLMClient(API_KEY, BASE_URL, MODEL_NAME)
    user_command = " ".join(user_command_input)
    if not user_command:
        logging.info(colored("Please provide a command description.", "yellow"))
        return

    logging.info(colored(f"User command received: '{user_command}'", "green"))

    suggested_commands = llm_client.get_command_suggestions(user_command)

    if suggested_commands:
        selected_command = interactive_command_selection(suggested_commands)

        if selected_command:
            logging.info(colored(f"\nSelected command: '{selected_command}'", "green"))
            # --- Optional: Execute the selected command ---
            try:
                process = subprocess.run(
                    selected_command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    check=True,
                )
                logging.info(colored("\nCommand output:", "green"))
                logging.info(process.stdout)
            except subprocess.CalledProcessError as e:
                logging.error(colored(f"\nError executing command:", "red"))
                logging.error(e.stderr)
            except FileNotFoundError:
                logging.error(
                    colored(f"\nError: Command not found: '{selected_command}'", "red")
                )
    else:
        logging.error(colored("Could not retrieve command suggestions.", "red"))


if __name__ == "__main__":
    cli()
