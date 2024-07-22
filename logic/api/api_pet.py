from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIPetStore:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def add_pet_to_the_store(self, pet_details):
        return self._request.post_request(f"{self._config['url']}", None, pet_details)

    def update_pet_in_the_store(self, pet_details):
        return self._request.put_request(f"{self._config['url']}", None, pet_details)

    def get_pets_by_status(self, status):
        return self._request.get_request(f"{self._config['url']}/findByStatus?status={status}")

    def get_pets_by_id(self, pet_id):
        return self._request.get_request(f"{self._config['url']}/{pet_id}")

    def update_pet_by_id(self, pet_id):
        return self._request.post_request(f"{self._config['url']}/{pet_id}")

    def delete_pet_by_id(self, pet_id):
        return self._request.delete_request(f"{self._config['url']}/{pet_id}")