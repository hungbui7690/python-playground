# (1) define classes called BankAccount and InsufficientFund classes in the bank_account.py module:
# (2) define the TestBankAccount class in the test_bank_account.py module: in this case, we use test_my_module.py


import unittest
from bank_account import BankAccount


# The TestBankAccount class has two test methods:
#
#     test_deposit() – test the deposit() method of the bank account.
#     test_withdraw() – test the withdraw() method of the bank account.
#
# Both methods create a new instance of the BankAccount. It’s redundant.
class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        self.bank_account = BankAccount(100)
        self.bank_account.deposit(100)
        self.assertEqual(self.bank_account.balance, 200)

    def test_withdraw(self):
        self.bank_account = BankAccount(100)
        self.bank_account.withdraw(50)
        self.assertEqual(self.bank_account.balance, 50)


# +++++++++++++++++++++++
# test_deposit (test_my_module.TestBankAccount.test_deposit) ... ok
# test_withdraw (test_my_module.TestBankAccount.test_withdraw) ... ok
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK
