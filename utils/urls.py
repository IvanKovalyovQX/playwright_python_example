def urls() -> dict[str, str]:
    return {
        "login_url": "https://rahulshettyacademy.com/client/#/auth/login",
        "registration_url": "https://rahulshettyacademy.com/client/#/auth/register",
        "api_registration_url": "https://rahulshettyacademy.com/api/ecom/auth/register",
        "api_login_url": "https://rahulshettyacademy.com/api/ecom/auth/login",
        "dashboard_url": "https://rahulshettyacademy.com/client/#/dashboard/dash",
    }


def headers() -> dict[str, str]:
    return {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://rahulshettyacademy.com",
        "Referer": "https://rahulshettyacademy.com/client/",
    }
