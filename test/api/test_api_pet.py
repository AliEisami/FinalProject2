import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.api_pet import APIPet


class TestAPIPet(unittest.TestCase):

    def setUp(self):
        # before tests (prepare tests)
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_from_file()
        self.api_pet = APIPet(self.api_request)
        self.api_pet.add_pet_to_the_store(self.config['pet_details'])

    def tearDown(self):
        # after tests (clean up)
        self.api_pet.update_pet_by_id(self.config["pet_details"]["id"])

    def test_add_pet_to_the_store(self):
        # test add pet to the store (POST)
        response = self.api_pet.add_pet_to_the_store(self.config['pet_details'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config['pet_details']["name"], response_body["name"])

    def test_update_pet_in_the_store(self):
        # test update pet in the store (PUT)
        response = self.api_pet.update_pet_in_the_store(self.config['updated_pet_details'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config['updated_pet_details']["name"], response_body["name"])

    def test_get_pets_by_status(self):
        # test find pet by status (GET)
        response = self.api_pet.get_pets_by_status(self.config['find_by_status'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response_body) >= 1)

    def test_get_pets_by_id(self):
        # test find pet by ID (GET)
        response = self.api_pet.get_pets_by_id(self.config["pet_details"]["id"])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body["name"], self.config["pet_details"]["name"])

    def test_update_pet_by_id(self):
        # test update pet by ID (PUT)
        response = self.api_pet.update_pet_by_id(self.config["pet_details"]["id"])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(self.config["pet_details"]["id"]), response_body["message"])

    def test_delete_pet_by_id(self):
        # test delete pet by ID (DELETE)
        response = self.api_pet.update_pet_by_id(self.config["pet_details"]["id"])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(self.config["pet_details"]["id"]), response_body["message"])
