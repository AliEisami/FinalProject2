import requests


class APIWrapper:
    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, headers=None, body=None):
        """Sends a GET request to the specified URL with optional headers and body.

        Args:
            url (str): The URL to send the GET request to.
            headers (dict, optional): The headers to include in the request.
            body (dict, optional): The body of the request, if any.

        Returns:
            Response: The response from the GET request.
        """
        return requests.get(url, headers=headers, json=body)

    @staticmethod
    def post_request(url, headers=None, body=None, file=None):
        """
        Sends a POST request to the specified URL with optional headers and body.

        Args:
            url (str): The URL to send the POST request to.
            headers (dict, optional): The headers to include in the request.
            body (dict, optional): The body of the request, if any.

        Returns:
            Response: The response from the POST request.
        """
        return requests.post(url, headers=headers, json=body, files=file)

    @staticmethod
    def put_request(url, headers=None, body=None):
        """
        Sends a PUT request to the specified URL with optional headers and body.

        Args:
            url (str): The URL to send the POST request to.
            headers (dict, optional): The headers to include in the request.
            body (dict, optional): The body of the request, if any.

        Returns:
            Response: The response from the PUT request.
        """
        return requests.put(url, headers=headers, json=body)

    @staticmethod
    def delete_request(url, headers=None, body=None):
        """
        Sends a DELETE request to the specified URL with optional headers and body.

        Args:
            url (str): The URL to send the POST request to.
            headers (dict, optional): The headers to include in the request.
            body (dict, optional): The body of the request, if any.

        Returns:
            Response: The response from the DELETE request.
        """
        return requests.delete(url, headers=headers, json=body)
