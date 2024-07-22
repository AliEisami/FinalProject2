import unittest
from infra.api.api_wrapper import APIWrapper
from infra.api.response_wrapper import ResponseWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.api.api_user import APIUser


class TestAPIUser(unittest.TestCase):

    def setUp(self):
        # before tests (prepare tests)
        self.api_request = APIWrapper()
        self.config = ConfigProvider.load_from_file()
        self.api_user = APIUser(self.api_request)
        self.api_user.create_list_of_users(self.config['users_list'])

    def tearDown(self):
        # after tests (clean up)
        self.api_user.delete_user_by_username(self.config['users_list'][0]['username'])

    def test_create_list_of_users(self):
        # test create a list of users (POST)
        response = self.api_user.create_list_of_users(self.config['users_list'])
        response_body = response.json()
        response_wrapper = ResponseWrapper(ok=response.ok, status_code=response.status_code, data=response.json())
        self.assertTrue(response_wrapper.ok)
        self.assertEqual(response_wrapper.status_code, 200)
        self.assertEqual(response_wrapper.data["message"], "ok")

    def test_find_user_by_username(self):
        # test get user by username (GET)
        response = self.api_user.find_user_by_username(self.config['users_list'][0]['username'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body["username"], self.config['users_list'][0]['username'])

    def test_delete_user_by_username(self):
        # test delete user by username (DELETE)
        response = self.api_user.delete_user_by_username(self.config['users_list'][0]['username'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_body["message"], self.config['users_list'][0]['username'])

    def test_login_user_successful(self):
        # test login with valid username and password (GET)
        response = self.api_user.login_user(self.config['users_list'][0]['username'],
                                            self.config['users_list'][0]['password'])
        response_body = response.json()
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertIn("logged in user session:", response_body["message"])
        self.api_user.logout_user()

    def test_login_user_unsuccessful(self):
        # BUG - test login with invalid username and password (GET)
        response = self.api_user.login_user(Utils.generate_random_string(5, 9),
                                            Utils.generate_random_string(7, 10))
        response_body = response.json()
        self.assertEqual(response.status_code, 404)
        self.assertIn("user not found", response_body["message"])
        self.api_user.logout_user()
