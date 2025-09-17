from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        email_inpuit = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        email_inpuit.fill("user.name@gmail.com")

        password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill("password")

        login_btn = chromium_page.get_by_test_id('login-page-login-button')
        login_btn.click()

        alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(alert).to_be_visible()
        expect(alert).to_have_text("Wrong email or password")
