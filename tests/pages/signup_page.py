from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # 10 seconds timeout

    FIRST_NAME = (By.XPATH, '//*[@id="wpforms-21010-field_1"]')
    LAST_NAME = (By.XPATH, '//*[@id="wpforms-21010-field_2"]')
    EMAIL = (By.XPATH, '//*[@id="wpforms-21010-field_4"]')
    PHONE = (By.XPATH, '//*[@id="wpforms-21010-field_5"]')
    COMPANY = (By.XPATH, '//*[@id="wpforms-21010-field_6"]')
    ROLE = (By.XPATH, '//*[@id="wpforms-21010-field_11"]')
    COUNTRY = (By.XPATH, '//*[@id="wpforms-21010-field_12"]')
    COMPANY_SIZE_BASE = "//select[@id='wpforms-21010-field_55']/option[text()='{}']"
    TERMS = (By.XPATH, '//*[@id="wpforms-21010-field_15_1"]')
    SUBMIT = (By.XPATH, '//*[@id="wpforms-submit-21010"]')

    def fill_signup_form(self, user):
        # Wait and fill each field
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME)).send_keys(user["first_name"])
        self.wait.until(EC.presence_of_element_located(self.LAST_NAME)).send_keys(user["last_name"])
        self.wait.until(EC.presence_of_element_located(self.EMAIL)).send_keys(user["email"])
        self.wait.until(EC.presence_of_element_located(self.PHONE)).send_keys(user["phone"])
        self.wait.until(EC.presence_of_element_located(self.COMPANY)).send_keys(user["company"])
        self.wait.until(EC.presence_of_element_located(self.ROLE)).send_keys(user["role"])
        self.wait.until(EC.presence_of_element_located(self.COUNTRY)).send_keys(user["country"])

        # Company size dropdown
        company_size_xpath = (By.XPATH, self.COMPANY_SIZE_BASE.format(user["company_size"]))
        self.wait.until(EC.presence_of_element_located(company_size_xpath)).click()
        # Terms button
        self.wait.until(EC.element_to_be_clickable(self.TERMS)).click()
        # Submit button
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT)).click()

