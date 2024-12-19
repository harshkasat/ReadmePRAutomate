import os
import requests
import subprocess
from config import BRANCH_NAME, COMMIT_MESSAGE, PR_TITLE, PR_BODY, GITHUB_TOKEN, GITHUB_USERNAME


def clone_github_repo(github_url, local_path):
    try:
        subprocess.run(['git', 'clone', github_url, local_path], check=True)
        print('Cloning github repo')
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository: {e}")
        return False

def chekout_github_repo(local_path):
    try:
        subprocess.run(['git', 'checkout', '-b', BRANCH_NAME], cwd=local_path, check=True)
        print('Checking out github repo')
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to checkout repository: {e}")
        return False

def commit_github_repo(local_path):
    try:
        # Set a default anonymous author configuration
        subprocess.run(
            ['git', 'config', 'user.email', 'noreply@example.com'],
            cwd=local_path,
            check=True
        )
        subprocess.run(
            ['git', 'config', 'user.name', 'Anonymous'],
            cwd=local_path,
            check=True
        )
        subprocess.run(['git', 'add', '.'], cwd=local_path, check=True)
        subprocess.run(['git', 'commit', '-m', COMMIT_MESSAGE], cwd=local_path, check=True)
        print('Committing github repo')
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit repository: {e}")
        return False

def create_update_readme_file(local_path, readme_markdown):
    try:
        readme_file_path = os.path.join(local_path, "README.md")
        with open(readme_file_path, "w") as readme_file:
            readme_file.write(readme_markdown)
        print('Created/updated README.md file')
        return readme_file_path
    except Exception as e:
        print(f"Failed to create/update README.md file: {e}")
        return None

def push_github_repo(local_path, repo):
    try:
        subprocess.run(['git', 'push', f'https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{repo}.git'], cwd=local_path, check=True)
        print('Push the github repo')
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to push repository: {e}")
        return False

def create_pull_request(owner, repo):
    try:
        api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        payload = {
            "title": PR_TITLE,
            "head": f'{GITHUB_USERNAME}:{BRANCH_NAME}',
            "base": 'main',
            "body": PR_BODY
        }

        # Send the POST request to create the PR
        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 201:
            print("Pull request created successfully!")
            print("PR URL:", response.json().get("html_url"))
            return response.json().get("html_url")
        else:
            print(f"Failed to create pull request: {response.status_code}")
            print(response.json())
            return None
    except Exception as e:
        print(f"Failed to create pull request: {e}")
        return None

def fork_repo(owner: str, repo_name: str) -> str:
    """
    This function forks a given repository on GitHub.

    Parameters:
    owner (str): The owner of the original repository.
    repo_name (str): The name of the repository.

    Returns:
    str: The URL of the forked repository if successful, otherwise None.
    """

    # GitHub API endpoint for forking
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/forks"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Send the POST request to fork the repo
    response = requests.post(api_url, headers=headers)

    if response.status_code == 202:
        forked_url = f"https://github.com/{GITHUB_USERNAME}/{repo_name}"
        print(f"Repository forked successfully! Forked repo: {forked_url}")
        return forked_url
    else:
        print(f"Failed to fork repository: {response.status_code}")
        print(response.json())
        return None
