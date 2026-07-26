import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
API_BASE_URL = f"{BASE_URL}/api"
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10"))
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
