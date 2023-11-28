from src.utils.utils import get_logger,run_shell_command
from pathlib import Path

DATA_UTILS_LOGGER = get_logger(Path(__file__).name)


def is_dvc_initialized():
    return (Path().cwd() / ".dvc").exists()



def initialize_dvc():
    if is_dvc_initialized():
        DATA_UTILS_LOGGER.info("DVC is already initialized")
        return
    DATA_UTILS_LOGGER.info("Initializing DVC")
    run_shell_command("dvc init")
    run_shell_command("dvc config core.analytics false")
    run_shell_command("dvc config core.autostage true")
    run_shell_command("git add .dvc")
    run_shell_command("git commit -nm 'Initialzied DVC' ")

def initialize_dvc_storage(dvc_remote_name:str, dvc_remote_url : str) :
    if not run_shell_command("dvc remote list"):
        DATA_UTILS_LOGGER.info("Initialize DVC storage")
        run_shell_command(f"dvc remote add -d {dvc_remote_name} {dvc_remote_url}")
        run_shell_command("git add .dvc/config")
        run_shell_command("git commit -nm 'Configured remote storage at: {dvc_remote_url}")
    else:
        DATA_UTILS_LOGGER.info("DVC storage was already initialized")

def commit_to_dvc(dvc_raw_data_folder,dvc_remote_name):
    current_version = run_shell_command("git tag --list | sort -t v -k 2 -g | tail -1 | sed 's/v//'").strip()
    if not current_version:
        current_version = "0"
    next_version = f"v{int(current_version)+1}"
    run_shell_command(f"dvc add {dvc_raw_data_folder}")
    run_shell_command("git add .")
    run_shell_command(f"git commit -nm 'Updated version fo the data from v{current_version } to {next_version}'")
    run_shell_command(f"git tag -a {next_version} -m 'Data version {next_version}'")
    run_shell_command(f"dvc push {dvc_raw_data_folder}.dvc --remote {dvc_remote_name}")
    run_shell_command("git push --follow-tags")
    run_shell_command("git push -f --tags")



def make_new_data_version(dvc_raw_data_folder:str, dvc_remote_name:str):
    try :
        status = run_shell_command(f"dvc status {dbc_raw_data_folder}.dvc") # check wether there is any change in dvc status
        if status == "Data and pipelines are up to date.\n":
            DATA_UTILS_LOGGER.info("Data and pipelines are upto date")
            return
        commit_to_dvc(dvc_raw_data_folder,dvc_remote_name)
    except CalledProcessError: # dvc not started . initial version 0
        commit_to_dvc(dvc_raw_data_folder,dvc_remote_name)
         