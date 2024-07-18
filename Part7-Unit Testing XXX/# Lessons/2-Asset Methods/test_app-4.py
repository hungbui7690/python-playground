import unittest

from app import Logger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_singleton(self):
        new_logger = Logger()
        self.assertIs(self.logger, new_logger)


# First, create a new instance of the Logger class in the setUp() method and assign it to the self.logger instance variable.
# Second, create a new instance of the Logger class and use the assertIs() method to check if two instances are the same.
