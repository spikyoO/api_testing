import requests
from endpoints.base_endpoint import BaseEndpoint


class UpdateObject(BaseEndpoint):

    def update_object(self, object_id, payload):
        self.response = requests.put(f"{self.url}/{object_id}", json=payload)
        self.response_json = self.response.json()

    def check_update(self, new_name, new_price):
        assert self.response_json["name"] == new_name and self.response_json["data"]["price"] == new_price
