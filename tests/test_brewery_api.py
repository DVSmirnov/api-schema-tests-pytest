import pytest

from helpers import assert_valid_response, get

BREWERIES_URL = "https://api.openbrewerydb.org/v1/breweries"


def test_get_brewery_by_id():
    # id берём из списка, а не зашиваем руками: идентификаторы со временем меняются
    brewery_id = get(BREWERIES_URL, params={"per_page": 1}).json()[0]["id"]

    response = get(f"{BREWERIES_URL}/{brewery_id}")

    data = assert_valid_response(response, "brewery.json")
    assert data["id"] == brewery_id


@pytest.mark.parametrize("city", ["San Diego"])
def test_breweries_by_city(city):
    response = get(BREWERIES_URL, params={"by_city": city, "per_page": 3})

    data = assert_valid_response(response, "brewery_list.json")
    assert 0 < len(data) <= 3
    assert all(brewery["city"] == city for brewery in data)


@pytest.mark.parametrize("name", ["dog", "cooperative"])
def test_breweries_by_name(name):
    response = get(BREWERIES_URL, params={"by_name": name, "per_page": 3})

    data = assert_valid_response(response, "brewery_list.json")
    assert 0 < len(data) <= 3
    assert all(name in brewery["name"].lower() for brewery in data)


@pytest.mark.parametrize("brewery_type", ["micro", "brewpub"])
def test_breweries_by_type(brewery_type):
    response = get(BREWERIES_URL, params={"by_type": brewery_type, "per_page": 3})

    data = assert_valid_response(response, "brewery_list.json")
    assert 0 < len(data) <= 3
    assert all(brewery["brewery_type"] == brewery_type for brewery in data)


@pytest.mark.parametrize("query", ["dog", "barrel", "brewing"])
def test_autocomplete(query):
    response = get(f"{BREWERIES_URL}/autocomplete", params={"query": query})

    data = assert_valid_response(response, "brewery_autocomplete.json")
    assert len(data) > 0
