from tests.Base import Base


class TestGetPet(Base):

    def test_get_pets(self, get_get_pet_url):
        self.assert_status_code(self.get_response(get_get_pet_url).status_code, 200)

    def test_inv(self, get_inv_url):
        self.assert_status_code(self.get_response(get_inv_url).status_code, 200)

