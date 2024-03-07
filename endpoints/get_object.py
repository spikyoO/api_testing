import requests
from endpoints.base_endpoint import BaseEndpoint


class GetObject(BaseEndpoint):

    def get_object_by_id(self, id):
        self.response = requests.get(f"{self.url}/{id}")
        self.response_json = self.response.json()

    def check_object_id(self, object_id):
        assert self.response_json["id"] == object_id
