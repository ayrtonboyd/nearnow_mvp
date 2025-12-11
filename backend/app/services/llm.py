from dotenv import load_dotenv
import os
import json
from pathlib import Path
from langchain_openai import ChatOpenAI
from app.services.data_loader import load_locations, load_tags

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load data once at app startup
locations = load_locations()
tags = load_tags()

# Path to system prompt
BASE_DIR = Path(__file__).resolve().parent.parent  # points to app/
SYSTEM_MESSAGE_PATH = BASE_DIR / "prompts" / "system_prompt.txt"



def load_system_message():
    """Reads the system prompt text file."""
    with open(SYSTEM_MESSAGE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def build_prompt(user_query: str):
    """Creates a unified prompt containing the system message, dataset, and user query."""
    system_message = load_system_message()

    prompt = f"""
{system_message}

Here is the dataset you must use:

LOCATIONS:
{json.dumps(locations, ensure_ascii=False, indent=2)}

TAGS:
{json.dumps(tags, ensure_ascii=False, indent=2)}

USER REQUEST:
"{user_query}"
"""
    return prompt


def run_llm(user_query: str):
    """Runs the LLM with the system prompt and dataset included."""

    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY is missing. Set it in your .env file as OPENAI_API_KEY=your_key_here"
        )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.4,
        api_key=OPENAI_API_KEY,
    )

    prompt = build_prompt(user_query)
    response = llm.invoke(prompt)

    return response.content
