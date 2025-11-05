import pytest
from playwright.sync_api import Playwright, Page, expect
from pages.authentification.registration_page import RegistrationPage


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page: # type: ignore
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page() # type: ignore
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    reistration_page = RegistrationPage(page=page)
    reistration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    reistration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    reistration_page.click_registration_button()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page: # type: ignore
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page # type: ignore
    browser.close()
