import requests
from endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):

    def new_object(self, payload):
        self.response = requests.post(self.url, json=payload)
        self.response_json = self.response.json()

    def check_name(self, name):
        assert self.response_json["name"] == name
