import pytest


@pytest.fixture()
def get_get_pet_url():
    return "http://localhost:8080/api/v3/pet/findByStatus?status=available"


@pytest.fixture()
def get_inv_url():
    return "http://localhost:8080/api/v3/store/inventory"


