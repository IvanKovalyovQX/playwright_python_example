# pyrefly: ignore[missing-import]
from playwright.sync_api import APIRequestContext

from .login_api import LoginApi
from .registration_api import RegistrationApi


class Api:
    def __init__(self, request: APIRequestContext):
        self.registration = RegistrationApi(request)
        self.login = LoginApi(request)
