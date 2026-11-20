# pyrefly: ignore[missing-import]
from playwright.sync_api import APIRequestContext, APIResponse

from utils.urls import headers, urls


class LoginApi:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def login(self, email: str, password: str) -> APIResponse:
        response = self.request.post(
            urls()["api_login_url"],
            headers=headers(),
            data={
                "userEmail": email,
                "userPassword": password,
            },
        )
        assert response.json()["message"] == "Login Successfully"
        token = response.json()["token"]
        return token
