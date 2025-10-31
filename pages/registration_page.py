from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_btn = page.get_by_test_id("registration-page-registration-button")
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def click_registration_btn(self):
        expect(self.registration_btn).to_be_enabled()
        self.registration_btn.click()
