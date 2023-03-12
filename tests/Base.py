import allure
import requests


class Base:

    @allure.step("getting response")
    def get_response(self, url):
        return requests.get(url)

    @allure.step("assset status code")
    def assert_status_code(self,actual,expected):
        assert actual == expected, f"Fail expected:{expected}, actual:{actual}"

