import unittest
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.api_store import APIStore


class TestAPIStore(unittest.TestCase):

    def setUp(self):
        # before tests (prepare tests)
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_from_file()
        self.api_store = APIStore(self.api_request)

    def tearDown(self):
        # after tests (clean up)
        self.api_store.delete_order_by_id(self.config['order']['id'])

    def test_get_store_inventory(self):
        # test get store inventory
        response = self.api_store.get_store_inventory()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)

    def test_place_order_for_purchasing(self):
        # test place order (POST)
        ConfigProvider.add_current_time_to_json()
        response = self.api_store.place_order_for_purchasing(self.config['order'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config['order']["petId"], response_body["petId"])

    def test_find_order_by_id_successful(self):
        # find order by valid ID (GET)
        self.api_store.place_order_for_purchasing(self.config['order'])
        response = self.api_store.find_order_by_id(self.config['order']['id'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.config['order']["id"], response_body["id"])

    def test_find_order_by_id_unsuccessful(self):
        # find order by invalid ID (GET)
        response = self.api_store.find_order_by_id(self.config['order']['id'])
        response_body = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_body["message"], "Order not found")

    def test_delete_order_by_id_successful(self):
        # delete order by valid ID (DELETE)
        self.api_store.place_order_for_purchasing(self.config['order'])
        response = self.api_store.delete_order_by_id(self.config['order']['id'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(self.config['order']["id"]), response_body["message"])

    def test_delete_order_by_id_unsuccessful(self):
        # delete order by invalid ID (DELETE)
        response = self.api_store.delete_order_by_id(self.config['order']['id'])
        response_body = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_body["message"], "Order Not Found")
