from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIUser:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def create_list_of_users(self, users_list):
        # create list of users
        return self._request.post_request(f"{self._config['url']}/user/createWithList", body=users_list)

    def find_user_by_username(self, username):
        # find user by username
        return self._request.get_request(f"{self._config['url']}/user/{username}")

    def delete_user_by_username(self, username):
        # delete user by username
        return self._request.delete_request(f"{self._config['url']}/user/{username}")

    def login_user(self, username, password):
        # login
        return self._request.get_request(f"{self._config['url']}/user/login?username={username}&password={password}")

    def logout_user(self):
        # logout
        return self._request.get_request(f"{self._config['url']}/user/logout")
