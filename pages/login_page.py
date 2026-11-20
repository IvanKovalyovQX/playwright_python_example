# pyrefly: ignore[missing-import]
from playwright.sync_api import Page

from utils.urls import urls


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.locator("#userEmail")
        self.password = page.locator("#userPassword")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self) -> None:
        self.page.goto(urls()["login_url"])

    def login(self, email: str, password: str) -> None:
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()
