import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()


WHITE = "\033[37m"
GREEN = "\033[32m"
RESET_COLOR = "\033[0m"
model_name = "gpt-3.5-turbo"


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
