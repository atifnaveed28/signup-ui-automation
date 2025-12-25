# Signup UI Automation Project

## Project Overview

This project automates the **Signup form** on [Userlytics](https://www.userlytics.com/userlytics-g/) using **Selenium WebDriver** and **pytest**.  
It demonstrates an **SDET-style automation framework** with:

- Page Object Model (POM)  
- Dynamic input from a config file  
- Explicit waits for stable interaction  
- Pytest test execution and reporting  

---

## Project Structure
signup-ui-automation/
│
├── tests/
│ ├── init.py
│ ├── conftest.py # WebDriver fixture
│ ├── pages/
│ │ ├── init.py
│ │ └── signup_page.py
│ └── test_signup_ui.py
├── utils/
│ ├── init.py
│ └── config.py # BASE_URL and TEST_USER data
├── pytest.ini
├── requirements.txt
└── README.md

Test Framework Features:
Page Object Model (POM): organizes locators and actions
Dynamic in
Explicit waits: ensures stable element interactions
Pytest fixtures: automatic browser setup/teardown

Notes:
Ignore Chrome [GCM] warnings — they do not affect test results.
Update locators in signup_page.py if the webpage changes.
Tests are designed to pass reliably on first run using explicit waits.

1: Clone the repository:
git clone <repo_url>
cd signup-ui-automation

2: Install dependencies:
pip install -r requirements.txt

3: Running the Tests:
pytest -v

4: Generate an HTML report:
pytest -v --html=report.html