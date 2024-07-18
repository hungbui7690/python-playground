# The following adds the tearDown() method to the TestBankAccount:

import unittest
from bank_account import BankAccount, InsufficientFund


class TestBankAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.bank_account = BankAccount(100)

    def test_deposit(self):
        self.bank_account.deposit(100)
        self.assertEqual(self.bank_account.balance, 200)

    def test_withdraw(self):
        self.bank_account.withdraw(50)
        self.assertEqual(self.bank_account.balance, 50)

    def tearDown(self) -> None:
        self.bank_account = None


# The tearDown() method assigns None to the self.bank_account instance.


# Summary
# Fixtures are functions and methods that execute before and after test code blocks execute.
# The setUpModule() and tearDownModule() run before and after all test methods in the module.
# The setUpclass() and tearDownClass() run before and after all test methods in a test class.
# The setUp() and tearDown() run before and after each test method of a test class.
