import unittest
from mock import Mock, patch
from app.mock.Account import Account
from requests.exceptions import ConnectionError


class TestMocking(unittest.TestCase):

    def test_mock_method_returns(self):
        my_mock = Mock()
        my_mock.my_method.return_value = 'hello'
        self.assertEqual("hello", my_mock.my_method())

    def test_account_return(self):
        account_data = {"id": 1, "name": "TestName"}
        mock_data_interface = Mock()
        mock_data_interface.get.return_value = account_data
        account = Account(mock_data_interface)

        self.assertDictEqual(account_data, account.get_account(1))

    def test_account_return_exception(self):
        mock_data_interface = Mock()
        mock_data_interface.get.side_effect = ConnectionError()
        account = Account(mock_data_interface)
        self.assertEqual('Connection error occurred. Try Again.',
                         account.get_account(1))

    @patch('app.mock.Account.requests')
    def test_get_current_balance(self, mock_request):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'Some text data'
        mock_request.get.return_value = mock_response
        account = Account(Mock())
        self.assertEqual(
            {'status': 200, 'data': 'Some text data'},
            account.get_current_balance(1)
        )


