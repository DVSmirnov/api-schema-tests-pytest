# api-schema-tests-pytest

Учебный проект по автоматизации тестирования API на Python.

Тесты ходят в три открытых REST API и проверяют, что сервис отвечает кодом 200 и что тело ответа
соответствует JSON-схеме (библиотека `jsonschema`):

- [Dog CEO](https://dog.ceo/dog-api/): породы и картинки собак;
- [Open Brewery DB](https://www.openbrewerydb.org/): пивоварни;
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/): посты, комментарии, задачи, фото.

Отдельный тест проверяет статус-код любого сайта, адрес и код задаются из командной строки.

## Запуск

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

На Mac и Linux активация такая: `source .venv/bin/activate`.

Проверить другой сайт и другой ожидаемый код:

```
pytest tests/test_ya_status.py --url https://ya.ru --status_code 200
```

Запустить тесты только одного сервиса:

```
pytest tests/test_dog_api.py
```

## Где что лежит

```
tests/              тесты по сервисам
  helpers.py        запрос с таймаутом и проверка ответа по схеме
  conftest.py       опции --url и --status_code
json_schemas/       схемы ответов (проверяют поля и типы, не конкретные значения)
```

