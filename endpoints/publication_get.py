import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class GetPublication(BaseEndpoint):

    @allure.step('Get publication')
    def get_publication(self, post_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{post_id}')
        self.statusik_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check id publication')
    def check_id_is_(self, post_id):
        assert self.response_json['id'] == post_id
        # print(self.response_json['id'])
