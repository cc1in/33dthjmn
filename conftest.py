import pytest
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    """Return the base URL for API tests"""
    return os.getenv("API_BASE_URL", "http://api.example.com")

@pytest.fixture(scope="session")
def api_key():
    """Return the API key for authentication"""
    return os.getenv("API_KEY", "your-api-key")

@pytest.fixture(scope="function")
def auth_headers(api_key):
    """Return common headers including authentication"""
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }