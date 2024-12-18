import os

CLIENT_PATH = os.path.dirname(os.path.abspath(__file__))
AUDIO_FOLDER = os.path.join(CLIENT_PATH, "audios")
IMAGES_FOLDER = os.path.join(CLIENT_PATH, "images")
PROFILE_IMAGES_FOLDER = os.path.join(IMAGES_FOLDER, "profiles")
API_URL: str = "http://localhost:8000"
API_BASE_ENDPOINT: str = "api/v1"
