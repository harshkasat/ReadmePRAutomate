from file_processing import load_and_index_files
from config import configure_llm
from utils import README_PROMPT, format_user_question
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from questions import ask_question, QuestionContext



def create_readme_file(github_url, local_path):
    repo_name = github_url.split("/")[-1]
    print("Cloning the repository...")
    index, documents, file_type_counts, filenames = load_and_index_files(local_path)
    if index is None:
        print("No documents were found to index. Exiting.")
        exit()

    print("Repository cloned. Indexing files...")
    llm = configure_llm()

    template = """
    Repo: {repo_name} ({github_url}) | Conv: {conversation_history} | Docs: {numbered_documents} | Q: {question} | FileCount: {file_type_counts} | FileNames: {filenames}

    Instr:
    1. Answer based on context/docs.
    2. Focus on repo/code.
    3. Consider:
        a. Purpose/features - describe.
        b. Functions/code - provide details/samples.
        c. Setup/usage - give instructions.
    4. Unsure? Say "I am not sure".

    Answer:
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["repo_name", "github_url", "conversation_history", "question", "numbered_documents", "file_type_counts", "filenames"]
    )

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    conversation_history = ""
    question_context = QuestionContext(index, documents, llm_chain, repo_name, github_url, conversation_history, file_type_counts, filenames)
    try:
        user_question = README_PROMPT
        print('Thinking...')
        user_question = format_user_question(user_question)

        answer = ask_question(user_question, question_context)
        return answer
    except Exception as e:
        print(f"An error occurred: {e}")