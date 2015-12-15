import unittest

from app.code.bank.account import Account


class AccountTest(unittest.TestCase):

    def test_create_valid_account(self):
        account = Account("001", 50)
        self.assertEqual(account.account_number, "001")
        self.assertEqual(account.balance, 50)

    def test_create_account(self):
        account = Account('001', 0)

