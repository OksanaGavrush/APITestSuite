# from test_project.endpoints.publication_create import CreatePublication
# from test_project.endpoints.publication_put import PutPublication
# from test_project.endpoints.publication_delete import DeletePublication
# from test_project.endpoints.publication_get import GetPublication


def test_create_publication(create_publication):

    # pub_create = CreatePublication()
    create_publication.create_post()
    create_publication.check_response_is_200()


def test_put_obj(post_id, put_publication):
    # put_publication = PutPublication()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
             }
        }
    put_publication.put_obj_by_id(post_id=post_id, payload=payload)
    put_publication.check_response_is_200()
    put_publication.check_name_is_(payload['name'])
    put_publication.check_shemas()


def test_delete_obj(post_id, delete_publication):
    # delete_obj = DeletePublication()
    delete_publication.delete_pub(post_id)
    delete_publication.check_response_is_200()


def test_get_obj(post_id, get_publication):
    # get_pub = GetPublication()
    get_publication.get_publication(post_id)
    get_publication.check_response_is_200()
    get_publication.check_id_is_(post_id)







