import os
import requests
import subprocess
from config import BRANCH_NAME, COMMIT_MESSAGE, PR_TITLE, PR_BODY, GITHUB_TOKEN, USERNAME


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

def push_github_repo(local_path):
    try:
        subprocess.run(['git', 'push', 'origin', BRANCH_NAME], cwd=local_path, check=True)
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
            "head": f'{USERNAME}:{BRANCH_NAME}',
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
        forked_url = f"https://github.com/{USERNAME}/{repo_name}"
        print(f"Repository forked successfully! Forked repo: {forked_url}")
        return forked_url
    else:
        print(f"Failed to fork repository: {response.status_code}")
        print(response.json())
        return None


def delete_forked_repo(repo_name: str) -> None:
    """
    This function deletes a forked repository on GitHub.

    Parameters:
    repo_name (str): The name of the forked repository to be deleted.

    Returns:
    None: This function does not return any value. It only prints a message indicating whether the deletion was successful or not.

    The function sends a DELETE request to the GitHub API endpoint for deleting a repository. If the request is successful (status code 204), it prints a message indicating that the repository was deleted successfully. If the request fails, it prints an error message containing the status code and the JSON response from the API.
    """

    # GitHub API endpoint for deleting a repository
    api_url = f"https://api.github.com/repos/{USERNAME}/{repo_name}"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Send the DELETE request to delete the repository
    response = requests.delete(api_url, headers=headers)

    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully!")
    else:
        print(f"Failed to delete repository: {response.status_code}")
        print(response.json())


if __name__ == "__main__":
#     # Call the function
    repo_url = "https://github.com/abhishekdumaniya/quiz-application"  # Replace with the repository you want to fork
#     # Extract the owner and repository name from the URL
    parts = repo_url.rstrip("/").split("/")
#     owner = parts[-2]
    repo_name = parts[-1]
#     # forked_repo = fork_repo(owner=owner, repo_name=repo_name)
    delete_forked_repo(repo_name=repo_name)
