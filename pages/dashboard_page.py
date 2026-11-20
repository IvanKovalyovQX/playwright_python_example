# pyrefly: ignore[missing-import]
from playwright.sync_api import Page, expect

from utils.urls import urls


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard = page.locator("#dashboard")

    def open(self) -> None:
        self.page.goto(urls()["dashboard_url"])

    def inject_token(self, token: str) -> None:
        if "rahulshettyacademy.com" not in self.page.url:
            self.page.goto(urls()["login_url"])
        self.page.evaluate(
            "(value) => localStorage.setItem('token', value)",
            token,
        )
        self.open()

    def expect_dashboard_visible(self) -> None:
        expect(self.page).to_have_url(urls()["dashboard_url"])
        expect(self.page.get_by_role("button", name="Sign Out")).to_be_visible()
