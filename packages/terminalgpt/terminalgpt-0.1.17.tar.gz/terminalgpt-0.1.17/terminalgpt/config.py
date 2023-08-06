import os
import platform

API_TOKEN_LIMIT = 4096

APP_NAME = "terminalgpt"
SECRET_PATH = f"~/.{APP_NAME}/{APP_NAME}.encrypted".replace(
    "~", os.path.expanduser("~")
)
KEY_PATH = f"~/.{APP_NAME}/{APP_NAME}.key".replace("~", os.path.expanduser("~"))

MODEL = "gpt-3.5-turbo"
ENCODING_MODEL = "cl100k_base"

INIT_SYSTEM_MESSAGE = {
    "role": "system",
    "content": f"""
You are a helpful personal assistant called "TerminalGPT" for a programer on a {platform.platform()} machine.
Please note that your answers will be displayed on the terminal.
So keep them short as possible (5 new lines max) and use a suitable format for printing on terminal.""",
}


INIT_WELCOME_MESSAGE = {
    "role": "user",
    "content": """
Please start with a random and short greeting message starts with 'Welcome to terminalGPT'.
Add a ton of self humor.
Keep it short as possible, one line.
""",
}
