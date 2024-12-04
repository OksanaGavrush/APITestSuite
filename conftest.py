import requests
import pytest
from endpoints.publication_create import CreatePublication
from endpoints.publication_delete import DeletePublication
from endpoints.publication_get import GetPublication
from endpoints.publication_put import PutPublication


@pytest.fixture()
def post_id(create_publication, delete_publication):
    # create_post_id = CreatePublication()
    create_publication.create_post()
    post_id_seave = create_publication.get_json_response['id']
    yield post_id_seave
    # DeletePublication().delete_pub(post_id_seave)
    delete_publication.delete_pub(post_id_seave)


@pytest.fixture()
def create_publication():
    return CreatePublication()


@pytest.fixture()
def put_publication():
    return PutPublication()


@pytest.fixture()
def get_publication():
    return GetPublication()


@pytest.fixture()
def delete_publication():
    return DeletePublication()



    # create_new_obj = {
    #     "name": "Apple",
    #     "data": {
    #         "year": 2024,
    #         "price": 1000,
    #         "CPU model": "Intel Core i9",
    #         "Hard disk size": "1 TB"
    #     }
    # }
    # response = requests.post('https://api.restful-api.dev/objects', json=create_new_obj)
    # create_id = response.json()["id"]
    # yield create_id
    # requests.delete(f'https://api.restful-api.dev/objects/{create_id}')