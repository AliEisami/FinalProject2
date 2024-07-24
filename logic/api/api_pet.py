from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.sql_setup import SQLSetup


class APIPet:

    def __init__(self, request: APIWrapper):
        self.endpoint = "pet"
        self._request = request
        self._config = ConfigProvider.load_from_file()
        self._database = SQLSetup(self._config['database'])
        self._database.create_connection()
        self._database.create_table(self._config['pet_table'])
        self._database.execute_query("DELETE from pets")

    def add_pet_to_the_store(self, pet_details):
        # add pet to the store
        response = self._request.post_request(f"{self._config['url']}/{self.endpoint}", None, pet_details)
        self._database.execute_query("INSERT INTO pets (name, category_id, status) VALUES (?, ?, ?)",
                                     (pet_details['name'], pet_details['category']['id'], pet_details['status']))
        return response

    def update_pet_in_the_store(self, pet_details):
        # update pet in the store
        return self._request.put_request(f"{self._config['url']}/{self.endpoint}", None, pet_details)

    def get_pets_by_status(self, status):
        # get pets by status
        return self._request.get_request(f"{self._config['url']}/{self.endpoint}/findByStatus?status={status}")

    def get_pets_by_id(self, pet_id):
        # grt prt by ID
        return self._request.get_request(f"{self._config['url']}/{self.endpoint}/{pet_id}")

    def update_pet_by_id(self, pet_id):
        # update pet by ID
        return self._request.post_request(f"{self._config['url']}/{self.endpoint}/{pet_id}")

    def delete_pet_by_id(self, pet_id):
        # delete pet by ID
        return self._request.delete_request(f"{self._config['url']}/{self.endpoint}/{pet_id}")
