from src.utils.utils import run_shell_command,get_logger
from pathlib import Path

DATA_UTILS_LOGGER = get_logger(Path(__file__).name)


def is_dvc_initialized():
    return (Path().cwd() / ".dvc").exists()



def initialize_dvc():
    if is_dvc_initialized():
        DATA_UTILS_LOGGER("DVC is already initialized")
        return
    DATA_UTILS_LOGGER("Initializing DVC")
    run_shell_command("dvc init")
    run_shell_command("dvc config core.analytics false")
    run_shell_command("dvc config core.autostage true")
    run_shell_command("git add .dvc")
    run_shell_command("git commit -nm 'Initialzied DVC' ")