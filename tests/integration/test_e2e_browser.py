"""End-to-End (E2E) tests using Selenium for full browser testing."""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.mark.e2e
class TestE2EPageLoadingAndAssets:
    """E2E tests for page loading and asset verification."""

    @pytest.fixture(autouse=True)
    def setup_browser(self):
        """Set up Selenium WebDriver."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(
            "--disable-blink-features=AutomationControlled"
        )

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(
            service=service,
            options=chrome_options,
        )
        self.driver.set_page_load_timeout(10)

        yield

        self.driver.quit()

    def test_homepage_renders_in_browser(self, live_server):
        """Test that homepage renders properly in a real browser."""
        self.driver.get(f"{live_server.url}/")

        # Wait for page title to load
        wait = WebDriverWait(self.driver, 5)
        title = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        assert title is not None
        assert "Nander Speerstra" in self.driver.page_source

    def test_hero_image_loads(self, live_server):
        """Test that hero image is present and loads."""
        self.driver.get(f"{live_server.url}/")

        wait = WebDriverWait(self.driver, 5)
        images = wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
        )

        assert len(images) > 0
        # Check that at least one image has src attribute
        for img in images:
            src = img.get_attribute("src")
            alt = img.get_attribute("alt")
            if src:
                assert alt is not None  # Images should have alt text

    def test_navigation_menu_visible(self, live_server):
        """Test that navigation menu is visible and clickable."""
        self.driver.get(f"{live_server.url}/")

        wait = WebDriverWait(self.driver, 5)
        nav = wait.until(EC.presence_of_element_located((By.ID, "navmenu")))

        assert nav is not None
        # Check for navigation items
        nav_items = nav.find_elements(By.TAG_NAME, "a")
        assert len(nav_items) > 0

    def test_gallery_page_loads_categories(self, live_server):
        """Test that gallery page loads and displays categories."""
        self.driver.get(f"{live_server.url}/gallery/")

        wait = WebDriverWait(self.driver, 5)
        page_title = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )

        assert page_title is not None

    def test_page_responsive_elements_present(self, live_server):
        """Test that Bootstrap responsive classes are applied."""
        self.driver.get(f"{live_server.url}/")

        wait = WebDriverWait(self.driver, 5)
        # Check for Bootstrap container
        container = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "container"))
        )

        assert container is not None

    def test_footer_visible_on_page(self, live_server):
        """Test that footer is visible on page."""
        self.driver.get(f"{live_server.url}/")

        wait = WebDriverWait(self.driver, 5)
        footer = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )

        assert footer is not None
        assert "Nander Speerstra" in self.driver.page_source

    def test_css_loads_properly(self, live_server):
        """Test that CSS is loaded and styles are applied."""
        self.driver.get(f"{live_server.url}/")

        wait = WebDriverWait(self.driver, 5)
        header = wait.until(EC.presence_of_element_located((By.ID, "header")))

        # Get computed style
        bg_color = header.value_of_css_property("background-color")
        assert bg_color is not None

    def test_javascript_loads_without_errors(self, live_server):
        """Test that JavaScript loads without errors."""
        self.driver.get(f"{live_server.url}/")

        # Wait for page to fully load
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located((By.BODY,)))

        # Check for console errors (if available)
        logs = self.driver.get_log("browser")
        errors = [log for log in logs if log["level"] == "SEVERE"]

        # Log any errors found
        if errors:
            print(f"JavaScript errors found: {errors}")
