import requests
import allure
from endpoints.base_endpoint import BaseEndpoint
import logging
logging.getLogger(__name__)

PAYLOAD = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
             }
        }


class CreatePublication(BaseEndpoint):

    @allure.step('Create post')
    def create_post(self, payload=None):
        payload = payload if payload else PAYLOAD
        logging.info(f"Информационное сообщение для теста.{payload}")
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.statusik_code = self.response.status_code
        self.get_json_response = self.response.json()

    def saved_response_json(self, name):
        assert self.get_json_response['name'] == name


