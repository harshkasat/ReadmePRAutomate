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
