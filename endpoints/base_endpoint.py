import requests
import allure


class BaseEndpoint:
    response = None
    statusik_code = None
    get_json_response = None

    @allure.step('Check status code is 200')
    def check_response_is_200(self):
        assert self.statusik_code == 200, 'Status code is not ok'
