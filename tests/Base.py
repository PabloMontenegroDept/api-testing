import allure
import requests
import pprint


class Base:

    @allure.step("getting response")
    def get_response(self, url):
        response =  requests.get(url)
        self.print_response(response)
        return response

    @allure.step("assset status code")
    def assert_status_code(self, actual, expected):
        assert actual == expected, f"Fail expected:{expected}, actual:{actual}"

    @allure.step("Printing Response")
    def print_response(self, response):
        pprint.pprint(response.json())


