from src.config_schemas.config_schema import Config
from src.utils.config_utils import get_config

# custom decorate created
@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None:
    print(config)


if __name__ == "__main__":
    version_data()  # type: ignore