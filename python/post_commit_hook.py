import git

def get_commit_history(repo_path):
    repo = git.Repo(repo_path)
    commits = list(repo.iter_commits('main'))  # Replace 'main' with your branch name
    for commit in commits:
        print(f"Commit: {commit.hexsha}")
        print(f"Author: {commit.author.name} <{commit.author.email}>")
        print(f"Date: {commit.committed_datetime}")
        print(f"Message: {commit.message}")
        print("\nChanged files:")
        for diff in commit.diff(commit.parents or None):
            print(f"{diff.change_type}: {diff.a_path} -> {diff.b_path}")
        print("\n---\n")

# Example usage
get_commit_history('/path/to/your/repo')
