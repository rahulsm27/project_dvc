# Repository about how to use DVC for data versioning.

DVC (Data Version Control) is a version control system designed specifically for handling large files and data sets. It works in conjunction with Git to version control your data files efficiently



1. The main code file is src-> version_data.py . 

2. The data is to be stored in folder raw

3. Use 'make build' command to build the docker image

4. Use 'make version-data' to run the src/version_data.py file

5. The GCP storge url is specified in src/config_schemas/config_schema.py

6. Upon exectuing the above command the code fetches the code will intialize the dvc if not initialized. IF it is already initialized it will skip the initialization process.

7. It will then fetch latest version number and automatically increment the version number by one. The new version is pushed to gcp storage  as specified in the config scehma configuration paratmeter.

The repo also demonstrates use of

1. Makefile

2. Poetry 

3. Use of code formatting tools like
    Lint,
    Import Sort
    Black
    Type Checking

4. Refer below section for details




----------------X------------------------------------X-----------
## MAKEFILE
Makefile can make running repetitive commands easier


----------------X------------------------------------X----
##  POETRY

Dependency resolution and locking of external libraries.

1. Depenency resolved. Final version stored in lock file
2. Create dependency groups and install packages within a specific dependency group.For test create one depenency group and for prodcution another.

In command line run below command to create pyproject.toml file 

1. poetry init 
2. specify dependenceis in pyporject.toml file
3. poetry install 
Use this command to install dependencies. It will automatically create a venv and install. Poetry makes project environment isolation one of its core features.

Creates a poetry.lock file. This file is automatically updated when poetry add is run to install new dependencies, poetry update is run to update dependency versions, or poetry lock is run to check for conflicts.
Poetry update

What this means is that it will always work isolated from your global Python installation. To achieve this, it will first check if it’s currently running inside a virtual environment. If it is, it will use it directly without creating a new one. But if it’s not, it will use one that it has already created or create a brand new one for you.

By default, Poetry will try to use the Python version used during Poetry’s installation to create the virtual environment for the current project.

4. poetry shell

poetry shell provides a shorthand to activate the virtual environment. By default Poetry doesn't create the venv within the project folder, but in {cache-dir}/virtualenvs . So using the activate script would require to find out the location of the venv everytime you want to activate it.

5. poetry update
To update any new dependencies in lock file
Fetches the latest matching versions for dependencies and updates the lock file with the new versions. This is similar to deleting the poetry.lock file and running poetry install again

6. poetry install --only main --syn

Command to update only main dependencies and not test

If there is already a poetry.lock file as well as a pyproject.toml file when you run poetry install, it means either you ran the install command before, or someone else on the project ran the install command and committed the poetry.lock file to the project (which is good).

Either way, running install when a poetry.lock file is present resolves and installs all dependencies that you listed in pyproject.toml, but Poetry uses the exact versions listed in poetry.lock to ensure that the package versions are consistent for everyone working on your project. As a result you will have all dependencies requested by your pyproject.toml file, but they may not all be at the very latest available versions (some dependencies listed in the poetry.lock file may have released newer versions since the file was created). This is by design, it ensures that your project does not break because of unexpected changes in dependencies.

The --sync can be combined with group-related options:

#dev docs are groups
poetry install --without dev --sync
poetry install --with docs --sync
poetry install --only dev

-----------------------------X----------------------------
## CODE FORMATING
Black - formats code as per pre defined standards 
black ./src

## IMPORTS SORING
ISORT - sort imports aplphabetcially and seperate into secitons and by type
isort ./src

## LINTING
FLAKE8 - linting toll that checks python codebase for errors styling issues
Doesn't support pyproject.toml. need to setup.cfg
flake8 ./src

## TYPE CHECKING
MYPY - type checks help ensure that we are usign variables and functions in code correctly

## CLI
mypy ./src

----------------X------------------------------------X-------------------------
## DOCKER COMPOSE
Docker Compose is a tool for running multi-container applications on Docker defined using the Compose file format. A Compose file is used to define how one or more containers that make up your application are configured. Once you have a Compose file, you can create and start your application with a single command: docker compose up.


----------------X------------------------------------X-------------------------
## PERMISION DENIED

sudo chown -R $(whoami) ~/.docker
sudo cmod +x ~./
