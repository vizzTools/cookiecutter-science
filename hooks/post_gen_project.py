import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

ENV_EXAMPLE = """# IMPORTANT: never ever include the .env to git. It contains sensitive information.

API_KEY_EXAMPLE=yourapikeyexample
"""

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def create_env_file():
    with open(os.path.join(PROJECT_DIRECTORY, ".env"), "w") as env_file:
        env_file.write(ENV_EXAMPLE)

if __name__ == "__main__":

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

    create_env_file()