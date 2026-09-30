import os
import shutil
import subprocess
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    path = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.exists(path):
        os.remove(path)


def remove_dir(dirpath):
    path = os.path.join(PROJECT_DIRECTORY, dirpath)
    if os.path.exists(path):
        shutil.rmtree(path)


def main():
    use_docker = "{{ cookiecutter.use_docker }}".lower() == "y"
    use_precommit = "{{ cookiecutter.use_precommit }}".lower() == "y"
    venv_name = "{{ cookiecutter.venv_name }}"

    if not use_docker:
        remove_dir("docker")
        remove_file(".dockerignore")

    if not use_precommit:
        remove_file(".pre-commit-config.yaml")

    # Initialize Git repository
    try:
        subprocess.run(["git", "init"], check=True, cwd=PROJECT_DIRECTORY)
        print("Initialized empty Git repository.")
    except Exception as e:
        print(f"Warning: Could not initialize git repository: {e}")

    # Create virtual environment using uv
    print(f"Creating virtual environment '{venv_name}' using uv...")
    try:
        subprocess.run(["uv", "venv", venv_name], check=True, cwd=PROJECT_DIRECTORY)
        print(f"Virtual environment '{venv_name}' created successfully.")
    except Exception as e:
        print(f"Warning: Failed to create virtual environment using uv: {e}")

    # Run uv sync --dev
    print("Installing dependencies using uv sync --dev...")
    env = os.environ.copy()
    if venv_name != ".venv":
        env["UV_PROJECT_ENVIRONMENT"] = os.path.join(PROJECT_DIRECTORY, venv_name)

    try:
        subprocess.run(["uv", "sync", "--dev"], check=True, cwd=PROJECT_DIRECTORY, env=env)
        print("Dependencies installed successfully.")
    except Exception as e:
        print(f"Warning: Failed to run 'uv sync --dev': {e}")

    # Generate initial migrations
    print("Generating initial database migrations...")
    try:
        subprocess.run(
            ["uv", "run", "python", "manage.py", "makemigrations"],
            check=True,
            cwd=PROJECT_DIRECTORY,
            env=env,
        )
        print("Initial migrations generated.")
    except Exception as e:
        print(f"Warning: Could not generate initial migrations: {e}")

    # Install pre-commit hooks if enabled
    if use_precommit:
        print("Installing pre-commit hooks...")
        try:
            subprocess.run(
                ["uv", "run", "pre-commit", "install"],
                check=True,
                cwd=PROJECT_DIRECTORY,
                env=env,
            )
            print("Pre-commit hooks installed successfully.")
        except Exception as e:
            print(f"Warning: Could not install pre-commit hooks: {e}")

    print("\n" + "=" * 60)
    print("🎉 Project '{{ cookiecutter.project_name }}' successfully generated!")
    print(f"📁 Location: {PROJECT_DIRECTORY}")
    print(f"🐍 Virtual Environment: {os.path.join(PROJECT_DIRECTORY, venv_name)}")
    print(f"💡 Activate venv: source {venv_name}/bin/activate")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
