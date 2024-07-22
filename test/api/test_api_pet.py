import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.api_pet_store import APIPetStore


class TestAPIPetStore(unittest.TestCase):

    def setUp(self):
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_from_file()
        self.api_pet_store = APIPetStore(self.api_request)

    def test_add_pet_to_the_store(self):
        response = self.api_pet_store.add_pet_to_the_store(self.config['pet_details'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config['pet_details']["name"], response_body["name"])

    def test_update_pet_in_the_store(self):
        response = self.api_pet_store.update_pet_in_the_store(self.config['pet_details'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config['pet_details']["category"]["name"], response_body["category"]["name"])

    def test_get_pets_by_status(self):
        response = self.api_pet_store.get_pets_by_status(self.config['find_by_status'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response_body) >= 1)

    def test_get_pets_by_id(self):
        response = self.api_pet_store.get_pets_by_id(self.config["pet_details"]["id"])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body["name"], self.config["pet_details"]["name"])

    def test_update_pet_by_id(self):
        response = self.api_pet_store.update_pet_by_id(self.config["pet_details"]["id"])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config["pet_details"]["id"], response_body["message"])

    def test_delete_pet_by_id(self):
        self.api_pet_store.add_pet_to_the_store(self.config['pet_details'])
        response = self.api_pet_store.update_pet_by_id(self.config["pet_details"]["id"])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config["pet_details"]["id"], response_body["message"])
