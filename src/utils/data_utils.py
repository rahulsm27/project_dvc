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
        run_shell_command("git commit -rm 'Configured remote storage at: {dvc_remote_url}")
    else:
        DATA_UTILS_LOGGER.info("DVC storage was already initialized")
         