import unittest
import json
import requests

from unittest.mock import patch, Mock
from src.config import Config
from src.todo_api_client import TodoApiClient

class TestTodoApiClient(unittest.TestCase):

    @patch('src.todo_api_client.requests.get')
    def test_get_todos_success(self, mock_get):
        expected_data = [{"id": 1, "title": "Test Todo", "completed": False}]
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_data
        mock_get.return_value = mock_response

        # Instantiate TodoApiClient
        api_client = TodoApiClient()

        # Call the method under test
        params = {'id': 1}
        result = api_client.get_todos(params)

        # Assertions
        mock_get.assert_called_once_with(f"{Config.API_ENDPOINT}todos", params=params)
        self.assertEqual(result, expected_data)

    @patch('src.todo_api_client.requests.get')
    def test_get_todos_http_error(self, mock_get):
        # Mock HTTP error response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.side_effect = requests.exceptions.RequestException("Test error")
        mock_get.return_value = mock_response

        # Instantiate TodoApiClient
        api_client = TodoApiClient()

        # Call the method under test
        params = {'key': 'value'}
        result = api_client.get_todos(params)

        # Assertions
        mock_get.assert_called_once_with(f"{Config.API_ENDPOINT}todos", params=params)
        self.assertIsNone(result)

    @patch('src.todo_api_client.requests.get')
    def test_get_todos_json_error(self, mock_get):
        # Mock response with JSON decoding error
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = json.JSONDecodeError("Test error", "", 0)
        mock_get.return_value = mock_response

        # Instantiate TodoApiClient
        api_client = TodoApiClient()

        # Call the method under test
        params = {'id': 1}
        result = api_client.get_todos(params)

        # Assertions
        mock_get.assert_called_once_with(f"{Config.API_ENDPOINT}todos", params=params)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()