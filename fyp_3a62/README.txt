fyp_3a62
========

Getting Started
---------------

- Change directory into your newly created project if not already there. Your
  current directory should be the same as this README.txt file and setup.py.

    cd fyp_3a62

- Create a Python virtual environment, if not already created.

    python -m venv env

- Execution Error

    run get-ExecutionPolicy to check if it is restricted
    run Set-ExecutionPolicy Unrestricted -Scope Process

- Start the Python virtual environment.

    For Windows Git Bash:
    source ./env/Scripts/activate

    For Windows Powershell:
    ./env/Scripts/activate

    For Linux:
    source ./env/bin/activate

- Upgrade packaging tools, if necessary.

    pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    pip install -e ".[testing]"

- Run your project.

    pserve development.ini
