import os

API_URL = os.environ.get("API_URL")
PROJECT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
)
