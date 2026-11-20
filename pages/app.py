# pyrefly: ignore[missing-import]
from playwright.sync_api import Page

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


class App:
    def __init__(self, page: Page):
        self.registration_page = RegistrationPage(page)
        self.login_page = LoginPage(page)
        self.dashboard_page = DashboardPage(page)
