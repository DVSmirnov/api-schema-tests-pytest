from helpers import get


def test_site_returns_expected_status_code(base_url, status_code):
    response = get(base_url)

    assert response.status_code == status_code
