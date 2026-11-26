import json
from pathlib import Path

import requests
from jsonschema import validate

SCHEMAS_DIR = Path(__file__).parent.parent / "json_schemas"
TIMEOUT = 10  # секунд: чтобы тест не завис, если сервис не отвечает


def get(url, params=None):
    """GET-запрос с таймаутом. Параметры запроса requests кодирует сам."""
    return requests.get(url, params=params, timeout=TIMEOUT)


def load_schema(file_name):
    with open(SCHEMAS_DIR / file_name, encoding="utf-8") as f:
        return json.load(f)


def assert_valid_response(response, schema_name, expected_status=200):
    """Проверяет статус-код, потом тело ответа по JSON-схеме.

    Статус проверяем первым: если сервис вернул ошибку, сразу видно статус и
    начало ответа, а не невнятное падение на разборе JSON.
    При несовпадении со схемой jsonschema сам бросает понятную ошибку,
    где видно, какое именно поле не подошло.
    Возвращает разобранный JSON, чтобы в тесте можно было проверить значения.
    """
    assert response.status_code == expected_status, (
        f"Ожидали статус {expected_status}, получили {response.status_code}: "
        f"{response.text[:200]}"
    )
    data = response.json()
    validate(instance=data, schema=load_schema(schema_name))
    return data
