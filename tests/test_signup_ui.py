# correct import
import time

from tests.pages.signup_page import SignupPage
from utils.config import BASE_URL, TEST_USER


class TestSignupUI:

    def test_signup_page_loads(self, driver):
        driver.get(BASE_URL)
        time.sleep(8)
        assert "User Experience Research Platform" in driver.title

    def test_valid_signup_submission(self, driver):
        driver.get(BASE_URL)
        signup = SignupPage(driver)
        signup.fill_signup_form(TEST_USER)

        # Basic validation (adjust if success message exists)
        assert "thank" in driver.page_source.lower() or "success" in driver.page_source.lower()
