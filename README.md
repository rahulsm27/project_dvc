# Repository about how to use DVC for data versioning.

DVC (Data Version Control) is a version control system designed specifically for handling large files and data sets. It works in conjunction with Git to version control your data files efficiently



1. The main code file is src-> version_data.py .

2. The data is to be stored in folder raw

3. Use 'make build' command to build the docker image

4. Use 'make version-data' to run the src/version_data.py file

5. The GCP storge url is specified in src/config_schemas/config_schema.py

6. Upon executing the above command the code fetches the code that will initialise the dvc if not initialized. If it is already initialized it will skip the initialization process.

7. It will then fetch the latest version number and automatically increment the version number by one. The new version is pushed to GCP storage as specified in the config schema configuration parameter.




The repo also demonstrates the use of

1. Makefile

2. Poetry

3. Use of code formatting tools like
Lint,
Import Sort
Black
Type Checking

4. Refer to below section for details




----------------X----------------X----------------X----------------
## MAKEFILE
Makefile can make running repetitive commands easier. A Makefile is a script used to automate the compilation and building of software projects.
Each rule in a Makefile consists of a target, dependencies, and commands.


----------------X----------------X----------------X----------------
## POETRY

Dependency resolution and locking of external libraries.

1. Dependency resolved. The final version is stored in lock file
2. Create dependency groups and install packages within a specific dependency group. For the test create one dependency group and for production another.

In the command line run the below command to create project.toml file

1. poetry init
2. specify dependencies in pyporject.toml file
3. poetry install->Use this command to install dependencies. It will automatically create a venv and install. Poetry makes project environment isolation one of its core features. It creates a poetry.lock file. This file is automatically updated when poetry add is run to install new dependencies,
poetry update is run to update dependency versions or poetry lock is run to check for conflicts. By default, Poetry will try to use the Python version used during Poetry’s installation to create the virtual environment for the current project.

4. poetry shell -> poetry shell provides a shorthand to activate the virtual environment. By default Poetry doesn't create the venv within the project folder, but in {cache-dir}/virtualenvs . So using the activate script would require finding out the location of the venv every time you want to activate it.

5. poetry update
To update any new dependencies in lock file
Fetches the latest matching versions for dependencies and updates the lock file with the new versions. This is similar to deleting the poetry.lock file and running poetry install again

6. poetry install --only main --syn

Command to update only main dependencies and not test If there is already a poetry.lock file as well as a pyproject.toml file when you run poetry install, it means either you ran the install command before, or someone else on the project ran the install command and committed the poetry.lock file to the project (which is good).

Either way, running install when a poetry.lock file is present resolves and installs all dependencies that you listed in pyproject.toml, but Poetry uses the exact versions listed in poetry.lock to ensure that the package versions are consistent for everyone working on your project. As a result you will have all dependencies requested by your pyproject.toml file, but they may not all be at the very latest available versions (some dependencies listed in the poetry.lock file may have released newer versions since the file was created). This is by design, it ensures that your project does not break because of unexpected changes in dependencies.

The --sync can be combined with group-related options:

#dev docs are groups
poetry install --without dev --sync
poetry install --with docs --sync
poetry install --only dev


----------------X----------------X----------------X----------------

## CODE FORMATING
Black - formats code as per pre defined standards
black ./src

## IMPORTS SORING
ISORT - sort imports alphabetically and seperate them into sections and by type
isort ./src

## LINTING
FLAKE8 - linting tool that checks Python codebase for errors and styling issues
Doesn't support pyproject.toml. need to setup.cfg
flake8 ./src

## TYPE CHECKING
MYPY-type checks help ensure that we are using variables and functions in code correctly

## CLI
mypy ./src


----------------X----------------X----------------X----------------
## DOCKER COMPOSE
Docker Compose is a tool for running multi-container applications on Docker defined using the Compose file format. A Compose file is used to define how one or more containers that make up your application are configured. Once you have a Compose file, you can create and start your application with a single command: docker compose up.



----------------X----------------X----------------X----------------
## PERMISSION DENIED

sudo chown -R $(whoami) ~/.docker
sudo cmod +x ~./