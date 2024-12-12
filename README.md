# ReadmePRAutomate

This project automates the process of generating a README file for a GitHub repository by analyzing the codebase and extracting relevant information.  It leverages Langchain for document loading, processing, and question answering, utilizing a Google Gemini AI model for natural language understanding.

## Purpose and Features

The primary purpose of `ReadmePRAutomate` is to create a comprehensive README.md file based on the contents of a given GitHub repository.  This automation reduces the manual effort required to write a README and ensures consistency across projects. Key features include:

* **Repository Cloning:** Clones a specified GitHub repository locally.
* **File Loading and Indexing:** Loads various file types (txt, md, py, ipynb, etc.) from the repository and indexes them using BM25Okapi and TF-IDF for efficient search.
* **Document Processing:** Splits large documents into smaller chunks for better processing.  Cleaning and tokenization are applied to the text.
* **Search Functionality:**  Allows searching the indexed documents based on a given query.  The search combines BM25 and TF-IDF scores for improved accuracy.
* **README Generation (Implicit):** While not explicitly generating a README in a single function, the code lays the groundwork for this.  The project analyzes the codebase and extracts information to eventually inform the creation of a README file. This would likely involve formulating questions about the project (e.g., "What is the purpose of this project?", "What are the main features?", "How do I set up this project?") and using the search functionality to answer them, then formatting those answers into a README structure.

## Functions and Code Details

The core functionality is distributed across several files:

**1. `requirements.txt`:** Lists the project's dependencies, including Langchain, various AI and NLP libraries, and data processing tools.  (See the provided list of packages above.)

**2. `app.py`:** The main entry point of the application.  It simply calls the `main` function (defined in `main.py`, not provided).

**3. `config.py`:** Contains configuration settings, including the Google Gemini API key, model name, and LLM configuration.  It initializes the `ChatGoogleGenerativeAI` LLM from the Langchain Google GenAI library.  Error handling is included to check for missing API keys and LLM initialization failures.  Example:

```python
genai_api_key = os.getenv('GEMINI_API_KEY')
os.environ['GOOGLE_API_KEY'] = os.getenv('GEMINI_API_KEY')
if genai_api_key is None:
    raise ValueError("Missing GEMINI_API_KEY environment variable")

def configure_llm():
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7, top_p=0.85)
        if llm is None:
            raise ValueError("LLM component is None")
        return llm
    except Exception as e:
        print(f"Failed to configure LLM: {e}")
        return None
```

**4. & 5. `file_processing.py`:** This file contains functions for:

* **`clone_github_repo(github_url, local_path)`:** Clones a GitHub repository using `subprocess.run`.  Handles potential errors during cloning.
* **`load_and_index_files(repo_path)`:** Loads files of various extensions from a given path, splits them into chunks using `RecursiveCharacterTextSplitter`, and creates a BM25Okapi index for efficient searching.  It also calculates TF-IDF vectors.  The function returns the index, split documents, file type counts, and a list of file sources.
* **`search_documents(query, index, documents, n_results=5)`:** Searches the indexed documents using both BM25 and TF-IDF cosine similarity, combines the scores, and returns the top `n_results` documents.


**Other Files:** The presence of `main.py`, `questions.py`, and `utils.py` suggests that these files contain the main logic for driving the application, defining the questions to ask about the repository, and utility functions respectively, but their content isn't provided.

## Setup and Usage

1. **Install Dependencies:**  Install the packages listed in `requirements.txt` using `pip install -r requirements.txt`.
2. **Set Environment Variables:** Set the `GEMINI_API_KEY` environment variable with your Google Gemini API key.
3. **Run the Application:** Execute `python app.py`.  (The exact execution details depend on the contents of `main.py`, which is not provided).  The application will likely require a GitHub repository URL as input.

**Note:**  The provided code snippets show only parts of the functionality.  The complete functionality relies on the interaction between all the files, especially the missing `main.py` which orchestrates the process.  The README generation aspect is implicit and would likely be implemented within `main.py` or a related file.