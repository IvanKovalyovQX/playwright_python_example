# Playwright Python

UI and API tests for the [Let's Shop](https://rahulshettyacademy.com/client) practice site. Tests use pytest and Playwright. Page interactions live in `pages/`, HTTP calls live in `api/`.

## Layout

| Path | Purpose |
| --- | --- |
| `tests/` | Pytest tests |
| `pages/` | Page objects (`App` wires registration, login, and dashboard) |
| `api/` | Playwright API requests for registration and login |
| `utils/dataSet.py` | User data for registration |
| `utils/urls.py` | Site URLs and request headers |
| `pytest.ini` | Pytest and Playwright options |
| `pyproject.toml` | Ruff formatting and lint settings |

## Setup

Python 3.15 is what this project is currently run with.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Run tests

`pytest.ini` runs Chromium headed and keeps screenshots, traces, and video when a test fails.

```bash
pytest
```

Run one test:

```bash
pytest tests/test_user_registration.py::test_registration_api
```

`test_user_creation` registers through the UI, logs in, and checks the dashboard. `test_registration_api` registers and logs in through the API, then opens the dashboard with the returned token.

## Style

```bash
ruff format api pages tests utils
ruff check api pages tests utils
```
