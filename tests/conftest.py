import pytest


@pytest.fixture()
def get_get_pet_url():
    return "https://petstore.swagger.io/v2/pet/findByStatus?status=available"


@pytest.fixture()
def get_inv_url():
    return "https://petstore.swagger.io/v2/store/inventory"


