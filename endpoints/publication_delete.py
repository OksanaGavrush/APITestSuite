import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class DeletePublication(BaseEndpoint):

    def delete_pub(self, post_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}')
        self.statusik_code = self.response.status_code

