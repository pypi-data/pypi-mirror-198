import argparse
import difflib
import json
import os
import subprocess
import sys
from typing import List, Dict, Any
from git2gpt.gpt4_interface import get_gpt4_suggestions
from git2gpt.core import apply_gpt_mutations, get_repo_snapshot, get_file_diff, get_tracked_files, commit_changes


def extract_mutations(suggestions: str) -> List[Dict[str, Any]]:
    if suggestions.startswith("```"):
        suggestions = suggestions[8:-3]  # strip the "```json\n" and "```"
    # gpt-4 seems to sometimes embed line feeds in json strings, which is illegal and breaks the parser.
    # this is a hack to avoid that by removing all linefeeds.
    suggestions = suggestions.replace("\n", " ")
    try:
        mutations = json.loads(suggestions)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        tempfile = 'error_log.json'
        with open(tempfile, 'w') as f:
            f.write(suggestions)
        print(f'Invalid suggestions saved to {tempfile} for debugging.')
        raise
    return mutations


def interact_with_gpt(snapshot: str, prompt: str, question: bool = False, temperature: float = 0.7) -> str:
    messages = [
        {
            "role": "system",
            "content": f"You are an impressive and thorough software development assistant. You reply only in JSON. Here is a snapshot of a repository: {snapshot}",
        },
        {
            "role": "system",
            "content": """Respond to the user's request with a list of mutations to apply to the repository, using the following JSON format.

Each mutation in the list must include an action, a file_path, and a content (for insert and update operations). The action can be one of the following strings: 'add', 'modify', 'delete'.
It is extremely important that you do not reply in any way but with an exact JSON string. Do not supply markup or any explanations outside of the code itself.
""",
        },
        {
            "role": "user",
            "content": f"Update the repostiory with the following changes: {prompt}" if not question else f"Answer these questions about the code: {prompt}"
        },
    ]
    print(f'Using prompt: {prompt}')
    return get_gpt4_suggestions(messages, temperature=temperature)


def display_diff(repo_path: str) -> None:
    tracked_files = get_tracked_files(repo_path)
    os.chdir(repo_path)
    for file in tracked_files:
        os.system(f'git diff --staged -- {file}')


def check_unstaged_changes(repo_path: str) -> bool:
    os.chdir(repo_path)
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    return bool(result.stdout.strip())


def main():
    parser = argparse.ArgumentParser(
        description="Modify a git repo using GPT-4 suggestions or ask a question about the code."
    )
    parser.add_argument(
        "--prompt",
        type=str,
        required=False,
        help="User prompt for specific desired changes"
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="Path to the git repository (default: current directory)",
    )
    parser.add_argument(
        "--ask",
        action="store_true",
        help="Ask a question about the code, rather than modify it",
    )
    parser.add_argument(
        "--editor",
        action="store_true",
        help="Open a temporary file with the user's preferred $EDITOR for providing the prompt",
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Force operation even with unstaged changes",
    )
    parser.add_argument(
        "-t", "--temperature",
        type=float,
        default=0.7,
        help="Specify the temperature for GPT-4 suggestions (default: 0.7)",
    )
    args = parser.parse_args()

    repo_path = args.repo
    prompt = args.prompt
    ask_question = args.ask
    force = args.force
    temperature = args.temperature

    if args.editor:
        import tempfile
        import subprocess
        editor = os.environ.get('EDITOR', 'vim')
        with tempfile.NamedTemporaryFile(suffix='.txt') as tmp:
            subprocess.call([editor, tmp.name])
            tmp.seek(0)
            prompt = tmp.read().decode('utf-8').strip()

    if not prompt:
        print('Error: No prompt provided. Please provide a prompt using --prompt or --editor.')
        sys.exit(1)

    if not force and check_unstaged_changes(repo_path):
        print('Error: Unstaged changes detected. Please commit or stash them before running this script. To force the operation, use -f/--force flag.')
        sys.exit(1)

    try:
        snapshot = get_repo_snapshot(repo_path)
        suggestions = interact_with_gpt(snapshot, prompt, question=ask_question, temperature=temperature)

        if ask_question:
            print(f'Answer: {suggestions}')
        else:
            mutations = extract_mutations(suggestions)
            apply_gpt_mutations(repo_path, mutations)
            display_diff(repo_path)
            decision = input("Do you want to keep the changes? (y/n): ")
            if decision.lower() == 'y':
                commit_changes(repo_path, f"git2gpt: {prompt}")
            else:
                print("No changes will be committed.")
                print("To discard the changes, run the following git command:")
                print("    git reset --hard HEAD")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
