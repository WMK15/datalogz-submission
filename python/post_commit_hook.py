import os
import git
import json

def get_commit_history(repo_path, branch_name='master'):
    """
    Retrieve commit history for a specific branch in a Git repository.
    
    :param repo_path: Path to the Git repository.
    :param branch_name: The branch name to retrieve commits from. Default is 'main'.
    :return: A list of commit objects.
    """
    repo = git.Repo(repo_path)
    commits = list(repo.iter_commits(branch_name))
    return commits

def parse_code_changes(commits):
    """
    Parse code changes from a list of commit objects.
    
    :param commits: A list of commit objects.
    :return: A list of dictionaries containing commit details and code changes.
    """
    parsed_commits = []
    
    for commit in commits:
        commit_info = {
            'commit_hash': commit.hexsha,
            'author': commit.author.name,
            'author_email': commit.author.email,
            'date': commit.committed_datetime.isoformat(),
            'message': commit.message.strip(),
            'changes': []
        }
        
        for diff in commit.diff(commit.parents or None):
            change_info = {
                'change_type': diff.change_type,
                'a_path': diff.a_path,
                'b_path': diff.b_path,
                'diff': diff.diff.decode('utf-8') if diff.diff else ''
            }
            commit_info['changes'].append(change_info)
        
        parsed_commits.append(commit_info)
    
    return parsed_commits

def format_data_as_json(parsed_commits, output_file):
    """
    Format commit data as JSON and save to a file.
    
    :param parsed_commits: List of dictionaries containing commit details and changes.
    :param output_file: Path to the output JSON file.
    """
    with open(output_file, 'w') as f:
        json.dump(parsed_commits, f, indent=4)
    print(f"Data saved to {output_file}")

def main():
    repo_path = "D:/PERSONAL/Projects/GitHub/headstarter/week5/hackathon/datalogz-submission"
    script_dir = os.path.join(repo_path, "python/.venv/Scripts")

    commits = get_commit_history(repo_path)
    parsed_commits = parse_code_changes(commits)
    format_data_as_json(parsed_commits, os.path.join(script_dir, 'commits_data.json'))

if __name__ == "__main__":
    main()
