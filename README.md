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
