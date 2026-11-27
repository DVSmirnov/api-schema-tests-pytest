import json
from pathlib import Path
import pytest

import requests
from jsonschema import validate

SCHEMAS_DIR = Path(__file__).parent.parent / "json_schemas"
TIMEOUT = 30  # секунд: чтобы тест не завис, если сервис не отвечает


def get(url, params=None):
    """GET-запрос с таймаутом."""

    response = requests.get(url, params=params, timeout=TIMEOUT)
    if response.status_code == 403 and "Just a moment" in response.text:
        pytest.skip(f"{url} закрыт защитой Cloudflare для этого IP")
    return response


def load_schema(file_name):
    with open(SCHEMAS_DIR / file_name, encoding="utf-8") as f:
        return json.load(f)


def assert_valid_response(response, schema_name, expected_status=200):
    """Проверяет статус-код, потом тело ответа по JSON-схеме."""

    assert response.status_code == expected_status, (
        f"Ожидали статус {expected_status}, получили {response.status_code}: "
        f"{response.text[:200]}"
    )
    data = response.json()
    validate(instance=data, schema=load_schema(schema_name))
    return data
