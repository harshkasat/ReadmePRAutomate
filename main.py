import tempfile
import time
from dotenv import load_dotenv
from llm_readme_response import create_readme_file
from pr_bot import clone_github_repo, chekout_github_repo, create_update_readme_file, \
    commit_github_repo, push_github_repo, create_pull_request, fork_repo

load_dotenv()

def readme_automate(github_url):
    
    try:
        with tempfile.TemporaryDirectory() as local_path:
            try:
                # Extract the owner and repository name from the URL
                parts = github_url.rstrip("/").split("/")
                owner = parts[-2]
                repo_name = parts[-1]
            except ValueError:
                print("Invalid GitHub repository URL.")
                return
            try:
                forked_url = fork_repo(owner=owner, repo_name=repo_name)
                time.sleep(0.7)
            except Exception as e:
                print(f"Failed to fork repository: {e}")
                return

            if clone_github_repo(forked_url, local_path):
                readme_markdown = create_readme_file(github_url=github_url, local_path=local_path)
                chekout_github_repo(local_path)
                create_update_readme_file(local_path, readme_markdown)
                commit_github_repo(local_path)
                push_github_repo(local_path, repo=repo_name)
                response = create_pull_request(owner=owner, repo=repo_name)
                return 'success' if response is not None else 'failed'
            else:
                return 'failed'
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'failed'
