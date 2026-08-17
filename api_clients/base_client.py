# api_clients/base_client.py
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from typing import Optional, Dict, Any

from core.config import settings
from core.logger import get_logger

logger = get_logger(__name__)

class BaseClient:
    """
    Base HTTP client providing a configured session, retries, and logging.
    All specific API clients should inherit from this.
    """
    def __init__(self, base_url: str = settings.base_api_url):
        self.base_url = base_url.rstrip('/')
        self.session = self._build_session()
        self.timeout = 10

    def _build_session(self) -> requests.Session:
        """Configures a session with robust retry logic."""
        session = requests.Session()

        session.trust_env = False 

        # Retry on 502, 503, 504 status codes up to 3 times
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Default headers for all requests
        session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        return session

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Wrapper around session.request to provide centralized logging and URL building.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        logger.info(f"API Request: {method} {url}")
        if 'json' in kwargs:
            logger.info(f"Payload: {kwargs['json']}")
            
        response = self.session.request(method, url, timeout=self.timeout, **kwargs)
        
        logger.info(f"API Response: {response.status_code} {response.reason}")
        # Log response body if it exists, truncating if it's massive
        if response.text:
            logger.info(f"Response Body: {response.text[:500]}...")
            
        return response