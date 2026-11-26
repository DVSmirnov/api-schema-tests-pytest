import pytest

from helpers import assert_valid_response, get

DOG_API = "https://dog.ceo/api"


def test_random_dog_image():
    response = get(f"{DOG_API}/breeds/image/random")

    data = assert_valid_response(response, "dog_image.json")
    assert data["status"] == "success"
    assert data["message"].startswith("https://")


@pytest.mark.parametrize("breed", ["affenpinscher", "african", "airedale", "akita"])
def test_sub_breeds_list(breed):
    response = get(f"{DOG_API}/breed/{breed}/list")

    data = assert_valid_response(response, "dog_list.json")
    assert data["status"] == "success"


@pytest.mark.parametrize(
    "count, breed",
    [(1, "hound"), (2, "akita"), (3, "hound")],
)
def test_several_random_images_of_breed(count, breed):
    response = get(f"{DOG_API}/breed/{breed}/images/random/{count}")

    data = assert_valid_response(response, "dog_list.json")
    assert len(data["message"]) == count


@pytest.mark.parametrize("breed", ["hound", "akita"])
def test_random_image_of_breed(breed):
    response = get(f"{DOG_API}/breed/{breed}/images/random")

    data = assert_valid_response(response, "dog_image.json")
    assert data["status"] == "success"


@pytest.mark.parametrize("breed, sub_breed", [("hound", "afghan")])
def test_sub_breed_images(breed, sub_breed):
    response = get(f"{DOG_API}/breed/{breed}/{sub_breed}/images")

    data = assert_valid_response(response, "dog_list.json")
    assert len(data["message"]) > 0
