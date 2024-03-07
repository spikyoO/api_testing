import requests
from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    def delete_obj(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")

    def check_message(self, object_id):
        assert f"id = {object_id} has been deleted" in self.response_json["message"]
