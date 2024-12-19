readme-file
# ReadmePRAutomate

**A GitHub Action to automatically generate a comprehensive README.md file for your project.**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://github.com/harshkasat/ReadmePRAutomate/actions/workflows/main.yml/badge.svg)](https://github.com/harshkasat/ReadmePRAutomate/actions/workflows/main.yml)


## Project Overview

`ReadmePRAutomate` is a GitHub Action designed to simplify the process of creating a comprehensive README file for your repositories.  It leverages Langchain to analyze your project's code and files, extracting key information to automatically populate a structured README.  This reduces the manual effort required for documentation, ensuring your projects are well-documented from the start.  The generated README includes sections covering prerequisites, installation, usage examples, and more.


## Table of Contents

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Project Architecture](#project-architecture)
* [Contributing](#contributing)
* [License](#license)


## Prerequisites

* A GitHub repository.
* A [Google Generative AI](https://generativeai.google/) API key (stored as the `GEMINI_API_KEY` environment variable).  This is crucial for the Langchain components to function.
* Python 3.9 or higher.  The project's dependencies are listed in `requirements.txt`.


## Installation

1.  **Install the GitHub Action:** Add the following workflow to your `.github/workflows` directory (e.g., `.github/workflows/readme.yml`):

```yaml
name: Generate README

on:
  push:
    branches:
      - main

jobs:
  generate-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: harshkasat/ReadmePRAutomate@main
        with:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }} # Replace with your secret
```

2.  **Add your API key as a GitHub Secret:**  Go to your repository's settings, navigate to "Secrets and variables" -> "Actions", and add a secret named `GEMINI_API_KEY` with your Google Generative AI API key.

3.  **Commit and Push:** Commit the changes to your repository. The action will automatically run on each push to the `main` branch.


## Usage

The action automatically generates a README.md file based on the files in your repository.  It uses Langchain to analyze the code and files, extracting information to populate the README's various sections.  The level of detail in the generated README depends on the content and structure of your project.


## Configuration

The main configuration is done through environment variables.  The most important is `GEMINI_API_KEY`, which is required for accessing the Google Generative AI API.  The `config.py` file contains settings for the LLM (currently using `gemini-1.5-flash`), temperature, and top_p parameters.  These can be adjusted to fine-tune the generated README.


## Project Architecture

The project consists of several Python files:

*   **`main.py`:** The main entry point of the action.
*   **`config.py`:** Contains configuration settings for the LLM and API key.
*   **`file_processing.py`:** Handles file loading, indexing, and searching using BM25Okapi and TF-IDF.  This file uses Langchain's `DirectoryLoader` and `NotebookLoader` to handle various file types.  It also employs `RecursiveCharacterTextSplitter` for text chunking.  Functions like `clone_github_repo`, `load_and_index_files`, and `search_documents` are defined here.
*   **`utils.py`:** (Not shown in provided code, but likely contains utility functions for text processing).


The action uses Langchain for LLM interaction, document loading, and text splitting.  It leverages BM25Okapi and TF-IDF for efficient document search and retrieval.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


**Note:**  The provided code snippets only show a portion of the project. The full functionality is more extensive, including functions for cleaning and tokenizing text (`clean_and_tokenize` in `file_processing.py`), which are essential for the search and indexing processes.  The `questions.py` file (not shown) likely contains prompts or questions used to guide the README generation process.  The actual README generation logic is not explicitly shown in the provided code.
=======
# ReadmePRAutomate

**A GitHub Action to automatically generate READMEs based on your repository's code and files.**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/harshkasat/ReadmePRAutomate/actions/workflows/main.yml/badge.svg)](https://github.com/harshkasat/ReadmePRAutomate/actions/workflows/main.yml)


## 1. Project Overview

ReadmePRAutomate is a GitHub Action designed to simplify the process of creating comprehensive README files for your projects. It analyzes your repository's code, extracts relevant information, and generates a structured README.md file. This action is particularly useful for projects with many files and complex structures, saving developers significant time and effort.  It leverages Langchain for natural language processing to help understand and summarize your project's contents.


## 2. Key Features

* **Automatic README generation:** Analyzes your repository and generates a README.md file.
* **Structured output:** Creates a well-organized README with sections for prerequisites, installation, usage, etc.
* **Langchain integration:** Uses Langchain for advanced text processing and summarization.
* **Customization:**  While the current implementation is hardcoded, future versions could allow for more customization of the README's content and structure.
* **GitHub Actions integration:** Seamlessly integrates into your GitHub workflow.


## 3. Table of Contents

* [Project Overview](#1-project-overview)
* [Key Features](#2-key-features)
* [Prerequisites](#4-prerequisites)
* [Installation](#5-installation-guide)
* [Usage](#7-usage-examples)
* [Project Architecture](#8-project-architecture)
* [License](#17-license)


## 4. Prerequisites

* A GitHub repository.
* A GitHub account with access to create GitHub Actions workflows.
* Python 3.7 or higher.
* The dependencies listed in `requirements.txt`.  These include various packages for text processing, natural language processing (Langchain, Google Generative AI), and file handling.


## 5. Installation Guide

1. **Create a GitHub Actions workflow:** Create a YAML file (e.g., `.github/workflows/readme-generation.yml`) in your repository.  The contents of this file will need to be developed to call the ReadmePRAutomate action.  This is not currently provided in the repository.

2. **Add the action:**  The workflow file will need to reference the ReadmePRAutomate action. This will require specifying the action's location (likely a GitHub repository). Again, this is not directly provided in the available code.

3. **Configure the action:** The action will likely require configuration options (not currently defined in the provided code) to specify which files to analyze and how to structure the generated README.


## 7. Usage Examples

The provided code does not contain a readily usable example of how to generate a README. The `main.py` file simply calls a `main` function from a separate `main.py` file (which is not provided). The core logic for README generation resides in `file_processing.py` and uses Langchain and Google Generative AI.  However,  the provided code snippets show the components:

**`file_processing.py` (Partial):**

This file contains functions to:

* `clone_github_repo`: Clones a GitHub repository locally using `git clone`.
* `load_and_index_files`: Loads files from a specified path, splits them into chunks, and creates a BM25Okapi index for efficient search.  It supports a wide range of file extensions.
* `search_documents`: Searches the indexed documents using a query, combining BM25 and TF-IDF scoring methods.


**Example Snippet (Illustrative - Requires Completion):**

The actual README generation would involve using the functions in `file_processing.py` to analyze the repository, extract relevant information, and format it into a Markdown structure.  This process is not fully implemented in the provided code.


## 8. Project Architecture

The project is composed of several Python files:

* `app.py`: Entry point for the application (currently incomplete).
* `config.py`: Contains configuration settings, including the Google Gemini API key.
* `file_processing.py`: Core logic for file loading, indexing, and searching.
* `main.py` (missing): Likely contains the main logic for README generation.
* `utils.py` (missing): Likely contains utility functions.


The architecture relies on Langchain for text processing and Google's Gemini API for potentially advanced text summarization or generation capabilities (depending on the missing `main.py` implementation).


## 17. License

MIT License
