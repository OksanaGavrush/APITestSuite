import requests
import allure
from endpoints.json_shemas import Publication
from endpoints.base_endpoint import BaseEndpoint


class PutPublication(BaseEndpoint):

    @allure.step("Prepare payload")
    def put_obj_by_id(self, post_id, payload=None):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{post_id}', json=payload)
        self.statusik_code = self.response.status_code
        self.get_json_response = self.response.json()

    @allure.step('Check name payload')
    def check_name_is_(self, name):
        assert self.get_json_response['name'] == name, 'Name is correct'

    @allure.step('Json shemas')
    def check_shemas(self):
        if self.get_json_response is not None:
            Publication(**self.get_json_response)
        else:
            assert False, "Response JSON is None"
