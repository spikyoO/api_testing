class BaseEndpoint:
    url = "https://api.restful-api.dev/objects"
    response = None
    response_json = None

    def check_status_code(self):
        assert self.response.status_code == 200
