import pytest
from playwright.sync_api import Playwright, Page
from pages.authentification.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest
import allure


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page: # type: ignore
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    yield context.new_page() # type: ignore
    
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='Trace', extension='zip')


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
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    yield context.new_page() # type: ignore
    
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()

    allure.attach.file(f'./tracing/{request.node.name}.zip', name='Trace', extension='zip')
