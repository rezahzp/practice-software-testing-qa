from sqlalchemy import create_engine, text
from core.config import settings
from core.logger import get_logger

logger = get_logger(__name__)

class DatabaseClient:
    """
    Client for interacting with the backend database.
    """
    def __init__(self):
        # We create the engine using the connection string from our .env
        self.engine = create_engine(settings.db_connection_string)

    def fetch_one(self, query: str, params: dict = None) -> dict:
        """Executes a SELECT query and returns a single row as a dictionary."""
        logger.info(f"Executing SQL: {query} with params: {params}")
        with self.engine.connect() as connection:
            result = connection.execute(text(query), params or {})
            row = result.fetchone()
            # Convert the row to a dictionary if it exists
            return row._mapping if row else None

# Instantiate a global instance to use in tests
db = DatabaseClient()