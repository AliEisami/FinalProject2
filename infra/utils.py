import json
import random
import string
from datetime import datetime
from infra.config_provider import ConfigProvider


class Utils:

    @staticmethod
    def generate_random_lowercase_string(min_length, max_length):
        """
            Generates a random string containing lowercase letters, digits.
            Args:
                min_length (int): The minimum length of the generated string.
                max_length (int): The maximum length of the generated string.
            Returns:
                str: A randomly generated string.
        """
        characters = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(characters) for _ in range(random.randint(min_length, max_length)))
        return username

    @staticmethod
    def generate_random_string(min_length, max_length):
        """
            Generates a random string containing uppercase and lowercase letters, digits.
            Args:
                min_length (int): The minimum length of the generated string.
                max_length (int): The maximum length of the generated string.
            Returns:
                str: A randomly generated string.
        """
        characters = string.ascii_letters + string.digits
        username = ''.join(random.choice(characters) for _ in range(random.randint(min_length, max_length)))
        return username