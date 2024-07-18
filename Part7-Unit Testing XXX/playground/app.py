"""
assertIs

Introduction to Python assertIs() method

- The assertIs() allows you to test if two objects are the same. The following shows the syntax of the assertIs() method:

  ~~ assertIs(first, second, msg=None)

- If the first and second reference the same object, the test will pass. Otherwise, it’ll fail.
- The msg is optional. It’s displayed in the test result in case the test fails.
- Technically, the assertIs() method uses the is operator:

    first is second

\\\\\\\\\\\\\\\\

- First, create a Logger singleton class in the app.py module:
- The singleton is a design pattern that limits the instantiation of a class to a single instance. In other words, you’ll have the same Logger object regardless of how many times you call the Logger() constructor.

"""

from datetime import datetime


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {message}')
