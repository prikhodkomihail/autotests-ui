from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from elements.button import Button
from elements.link import Link
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page, "registration-page-registration-button", "Register")
        self.login_link = Link(page, 'registration-page-login-link', "Login")

    def click_registration_btn(self):
        self.registration_button.check_enabled()
        self.registration_button.click()
