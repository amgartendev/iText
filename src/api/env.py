import os

from dotenv import load_dotenv

loaded_dotenv = load_dotenv()

if not loaded_dotenv:
    raise SystemExit("No environment file detected, exiting...")


def get_env_variable_or_exit(key: str):
    value = os.environ.get(key, None)
    if value is None:
        raise SystemExit(f'No Environment Variable with key "{key}". Exiting...')
    return value


DEVELOPER_MODE = bool(os.environ.get("DEV_MODE", False))
SQLALCHEMY_DATABASE_URL = get_env_variable_or_exit("SQLALCHEMY_DATABASE_URL")
DB_REBUILD = DEVELOPER_MODE and bool(os.environ.get("DB_REBUILD", False))
DB_TEST_VALUES = (DEVELOPER_MODE and DB_REBUILD and bool(os.environ.get("DB_TEST_VALUES", False)))
