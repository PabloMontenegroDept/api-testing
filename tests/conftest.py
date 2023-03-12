import pytest
from config.url import url, endpoint


@pytest.fixture()
def get_get_pet_url():
    return url+endpoint["pet"]

