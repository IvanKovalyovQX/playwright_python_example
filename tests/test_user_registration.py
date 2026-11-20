# pyrefly: ignore[missing-import]


# pyrefly: ignore[missing-import]
from playwright.sync_api import Page

from api.api import Api
from pages.app import App
from utils.dataSet import registration_user


def test_user_creation(page: Page):
    user = registration_user()
    app = App(page)

    app.registration_page.open()
    createdUser = app.registration_page.registerUser(
        user["first_name"],
        user["last_name"],
        user["email"],
        user["mobile"],
        user["password"],
    )
    app.registration_page.expect_account_created()
    app.login_page.open()
    app.login_page.login(createdUser, user["password"])
    app.dashboard_page.expect_dashboard_visible()


def test_registration_api(page: Page):
    user = registration_user()
    app = App(page)
    api = Api(page.request)

    userEmail = api.registration.register()
    token = api.login.login(userEmail, user["password"])
    app.login_page.open()
    app.dashboard_page.inject_token(token)
    app.dashboard_page.expect_dashboard_visible()
