"""
============================================================
PROJECT : Healthy Breakfast Ideas Generator
FILE    : breakfast.py
MODEL   : gpt-4o-mini

DESCRIPTION:
    This application uses LangChain and OpenAI to generate
    exactly five healthy breakfast ideas.

    The program demonstrates:
    1. Loading an OpenAI API key from environment variables.
    2. Using LangChain's ChatOpenAI.
    3. Writing a precise prompt.
    4. Calling the model using invoke().
    5. Extracting text from an AIMessage using .content.
    6. Observing response variation across executions.
============================================================
"""


# ============================================================
# SECTION 1: IMPORT REQUIRED LIBRARIES
# ============================================================

# os is used to access environment variables.
import os

# pathlib helps locate the .env file.
from pathlib import Path

# load_dotenv loads configuration from the .env file.
from dotenv import load_dotenv

# ChatOpenAI connects LangChain to OpenAI models.
from langchain_openai import ChatOpenAI


# ============================================================
# SECTION 2: LOAD ENVIRONMENT VARIABLES
# ============================================================

def load_environment():
    """
    Load the OpenAI API key from the .env file.

    The API key is never hard-coded in the Python program.
    """

    base_dir = Path(__file__).resolve().parent

    env_file = base_dir / ".env"

    if not env_file.is_file():
        raise FileNotFoundError(
            f".env file not found: {env_file}"
        )

    load_dotenv(dotenv_path=env_file)

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError(
            "OPENAI_API_KEY is missing from the environment."
        )


# ============================================================
# SECTION 3: INITIALIZE THE LANGUAGE MODEL
# ============================================================

def initialize_model():
    """
    Initialize OpenAI using LangChain's ChatOpenAI.

    temperature=0.7:
        Allows some variation in generated responses.

    The same prompt may produce different breakfast ideas
    across multiple executions.
    """

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7
    )

    return llm


# ============================================================
# SECTION 4: DEFINE THE PROMPT
# ============================================================

def get_prompt():
    """
    Create a precise prompt requesting exactly five
    healthy breakfast ideas.

    The prompt explicitly defines the output format.
    """

    prompt = """
Suggest exactly 5 healthy breakfast ideas.

Formatting requirements:
1. Number the ideas from 1 to 5.
2. Write exactly one breakfast idea per line.
3. Keep each idea short, specific, and nutritious.
4. Do not include an introduction or conclusion.
5. Do not include explanations or additional text.
"""

    return prompt.strip()


# ============================================================
# SECTION 5: GENERATE BREAKFAST IDEAS
# ============================================================

def generate_breakfast_ideas(llm, prompt):
    """
    Send the prompt to OpenAI using LangChain.

    IMPORTANT:
        llm.invoke(prompt) returns an AIMessage object.

        response.content extracts the generated text.

    We print only the response content, not the entire
    AIMessage object.
    """

    response = llm.invoke(prompt)

    print(response.content)


# ============================================================
# SECTION 6: MAIN APPLICATION
# ============================================================

def main():
    """
    Main application workflow:

    1. Load environment variables.
    2. Initialize ChatOpenAI.
    3. Prepare the breakfast prompt.
    4. Generate and print five breakfast ideas.
    """

    load_environment()

    llm = initialize_model()

    prompt = get_prompt()

    generate_breakfast_ideas(llm, prompt)


# ============================================================
# SECTION 7: APPLICATION ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()