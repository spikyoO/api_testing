import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

@pytest.fixture(scope='session')
def obj_id() -> object:
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_obj = CreateObject()
    create_obj.new_object(payload)
    yield create_obj.response_json["id"]
    delete_obj = DeleteObject()
    delete_obj.delete_obj(create_obj.response_json["id"])
    delete_obj.check_status_code()
