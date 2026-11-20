# pyrefly: ignore[missing-import]
from playwright.sync_api import APIRequestContext, APIResponse

from utils import dataSet
from utils.urls import headers, urls


class RegistrationApi:
    def __init__(self, request: APIRequestContext):
        self.request = request

    def register(
        self,
        first_name: str = dataSet.registration_user()["first_name"],
        last_name: str = dataSet.registration_user()["last_name"],
        email: str = dataSet.registration_user()["email"],
        mobile: str = dataSet.registration_user()["mobile"],
        password: str = dataSet.registration_user()["password"],
        occupation: str = "Scientist",
        gender: str = "Male",
    ) -> APIResponse:
        response = self.request.post(
            urls()["api_registration_url"],
            headers=headers(),
            data={
                "firstName": first_name,
                "lastName": last_name,
                "userEmail": email,
                "userRole": "customer",
                "occupation": occupation,
                "gender": gender,
                "userMobile": mobile,
                "userPassword": password,
                "confirmPassword": password,
                "required": True,
            },
        )
        assert response.json()["message"] == "Registered Successfully"
        return email
