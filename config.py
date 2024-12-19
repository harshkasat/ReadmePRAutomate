import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


BRANCH_NAME = 'readme-file'
COMMIT_MESSAGE = 'Update README.md: Add installation instructions'
PR_TITLE = 'Update README.md: Add installation instructions'
PR_BODY = 'This PR updates the README.md file by adding a section with detailed installation instructions for different operating systems.'
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

genai_api_key = os.getenv('GEMINI_API_KEY')
os.environ['GOOGLE_API_KEY'] = os.getenv('GEMINI_API_KEY')
if genai_api_key is None:
    raise ValueError("Missing GEMINI_API_KEY environment variable")


# Initialize the API client
def configure_llm():
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
            temperature=0.7, top_p=0.85)
        if llm is None:
            raise ValueError("LLM component is None")
        return llm
    except Exception as e:
        print(f"Failed to configure LLM: {e}")
        return None
