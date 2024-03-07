from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject


def test_create_object():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload)
    new_object_endpoint.check_name(payload["name"])
    new_object_endpoint.check_status_code()


def test_get_object(obj_id):
    get_object_endpoint = GetObject()
    get_object_endpoint.get_object_by_id(obj_id)
    get_object_endpoint.check_status_code()
    get_object_endpoint.check_object_id(obj_id)


def test_update_object(obj_id):
    payload = {
        "name": "Apple MacBook Pro New",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    update_object_endpoint = UpdateObject()
    update_object_endpoint.update_object(obj_id, payload)
    update_object_endpoint.check_update(payload["name"], payload["data"]["price"])
    update_object_endpoint.check_status_code()

