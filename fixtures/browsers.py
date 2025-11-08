import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright

from pages.authentification.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page: # type: ignore
    yield from initialize_playwright_page(playwright, test_name=request.node.name) # type: ignore


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
def chromium_page_with_state(request: SubRequest, initialize_browser_state, playwright: Playwright) -> Page: # type: ignore
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state="browser-state.json"
    ) # type: ignore
