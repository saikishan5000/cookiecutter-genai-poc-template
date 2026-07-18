import os
import shutil
import subprocess
import sys

def remove_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)

def init_git():
    try:
        subprocess.check_call(["git", "init"])
        subprocess.check_call(["git", "add", "."])
        subprocess.check_call(["git", "commit", "-m", "Initial commit from cookiecutter template"])
        print("Git repository initialized successfully.")
    except Exception as e:
        print(f"Warning: Failed to initialize Git repository: {e}", file=sys.stderr)

def main():
    env_manager = "{{ cookiecutter.environment_manager }}"

    if env_manager == "venv":
        remove_file("environment.yml")
    elif env_manager == "conda":
        remove_file("requirements.txt")
    
    # Initialize git repo
    init_git()

if __name__ == "__main__":
    main()
