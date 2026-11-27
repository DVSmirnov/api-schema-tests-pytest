import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://example.com",
        help="Адрес сайта, который проверяем",
    )
    parser.addoption(
        "--status_code",
        default=200,
        type=int,  # без type=int из командной строки приходит строка "404"
        help="Ожидаемый статус-код ответа",
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
