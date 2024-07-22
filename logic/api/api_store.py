from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIStore:
    def __init__(self, request: APIWrapper):
        self._request = request
        self._config = ConfigProvider.load_from_file()

    def get_store_inventory(self):
        # get store inventory
        return self._request.get_request(f"{self._config['url']}/store/inventory")

    def place_order_for_purchasing(self, order):
        # post an order
        return self._request.post_request(f"{self._config['url']}/store/order", body=order)

    def find_order_by_id(self, order_id):
        # get order by ID
        return self._request.get_request(f"{self._config['url']}/store/order/{order_id}")

    def delete_order_by_id(self, order_id):
        # delete an order by ID
        return self._request.delete_request(f"{self._config['url']}/store/order/{order_id}")
