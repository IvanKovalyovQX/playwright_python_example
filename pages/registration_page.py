# pyrefly: ignore[missing-import]
from playwright.sync_api import Page, expect

from utils.urls import urls


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator("#firstName")
        self.last_name = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.mobile = page.locator("#userMobile")
        self.occupation = page.get_by_role("combobox")
        self.password = page.locator("#userPassword")
        self.confirm_password = page.locator("#confirmPassword")
        self.age_confirmation = page.get_by_role("checkbox")
        self.register_button = page.get_by_role("button", name="Register")

    def open(self) -> None:
        self.page.goto(urls()["registration_url"])

    def registerUser(
        self, first_name: str, last_name: str, email: str, mobile: str, password: str
    ) -> None:
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.email.fill(email)
        self.mobile.fill(mobile)
        self.occupation.select_option(label="Engineer")
        self.page.get_by_role("radio", name="Male", exact=True).check()
        self.password.fill(password)
        self.confirm_password.fill(password)
        self.age_confirmation.check()
        self.register_button.click()
        return email

    def expect_account_created(self) -> None:
        expect(self.page.get_by_text("Account Created Successfully")).to_be_visible()
