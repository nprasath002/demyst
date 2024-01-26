import unittest

from src.config import Config


class TestConfig(unittest.TestCase):
    def test_api_endpoint(self):
        self.assertEqual(Config.API_ENDPOINT, "https://jsonplaceholder.typicode.com/")  # add assertion here


if __name__ == '__main__':
    unittest.main()
