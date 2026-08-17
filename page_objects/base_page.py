from playwright.sync_api import Page
from core.logger import get_logger

logger = get_logger(__name__)

class BasePage:
    """
    Base class for all Page Objects.
    Contains common Playwright interactions and waits.
    """
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        logger.info(f"Navigating to {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def click(self, selector: str):
        logger.info(f"Clicking element: {selector}")
        self.page.locator(selector).click()

    def fill_text(self, selector: str, text: str):
        logger.info(f"Filling '{text}' into {selector}")
        self.page.locator(selector).fill(text)

    def is_visible(self, selector: str) -> bool:
        logger.info(f"Checking visibility of: {selector}")
        return self.page.locator(selector).is_visible()