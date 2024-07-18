# To avoid redundancy, you can create an instance of the BankAccount class in setUp() method and use it in all the test methods:


import unittest
from bank_account import BankAccount


# In the setUp() method:
# First, create an instance of the BankAccount class and assign it to the instance variable self.bank_account.
# Then, use self.bank_account instance in both test_deposit() and test_withdraw() methods.
class TestBankAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.bank_account = BankAccount(100)

    def test_deposit(self):
        self.bank_account.deposit(100)
        self.assertEqual(self.bank_account.balance, 200)

    def test_withdraw(self):
        self.bank_account.withdraw(50)
        self.assertEqual(self.bank_account.balance, 50)


# When running test methods test_deposit() and test_withdraw(), the setUp() runs before each test method.
# For test_deposit() method:
# - setUp()
# - test_deposit()
# For test_withdraw() method:
# - setUp()
# - test_withdraw()


# +++++++++++++++++++
# test_deposit (test_bank_account.TestBankAccount) ... ok
# test_withdraw (test_bank_account.TestBankAccount) ... ok
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK
