import time


def registration_user() -> dict[str, str]:
    return {
        "first_name": "Test",
        "last_name": "User",
        "email": f"user.{int(time.time())}@example.com",
        "mobile": "9876543210",
        "password": "Test@1234",
    }
