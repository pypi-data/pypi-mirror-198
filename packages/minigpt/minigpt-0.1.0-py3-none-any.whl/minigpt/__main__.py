import os
import sys

import minigpt
import pyperclip
import typer
from minigpt import speech_to_text
from typer import Option

app = typer.Typer(help="Chat with ChatGPT")


def configure_api_key(api_key=None):
    minigpt.api_key = api_key or os.environ.get("MINIGPT_API_KEY")
    if not minigpt.api_key:
        raise Exception("API key required")


def get_chat_prompt():
    """Get chat prompt based on the command invocation method."""
    if not os.isatty(0):
        prompt = sys.stdin.read()
    else:
        prompt = speech_to_text()
    return prompt


@app.command(help="Prompt ChatGPT and get a response")
def chat(
        api_key: str = Option(None,
                              help="API key to use. Overrides MINIGPT_API_KEY."),
        copy: bool = Option(False, help="Copy response to clipboard"),
):
    configure_api_key(api_key)
    prompt = get_chat_prompt()
    response = minigpt.get_response(prompt)

    print(response)
    if copy:
        pyperclip.copy(response)


@app.command(help="Convert speech to text")
def textify(
        api_key: str = Option("",
                              help="API key to use. Overrides MINIGPT_API_KEY."),
        copy: bool = Option(False, help="Copy response to clipboard"),
):
    configure_api_key(api_key)
    response = speech_to_text()
    print(response)
    if copy:
        pyperclip.copy(response)


def main():
    app()


main()