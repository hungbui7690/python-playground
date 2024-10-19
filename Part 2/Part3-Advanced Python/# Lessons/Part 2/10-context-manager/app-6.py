"""
Python context manager applications

- As you see from the previous example, the common usage of a context manager is to open and close files automatically.
- However, you can use context managers in many other cases:


    1) Open – Close
    - If you want to open and close a resource automatically, you can use a context manager.
    - For example, you can open a socket and close it using a context manager.

    2) Lock – release
    - Context managers can help you manage locks for objects more effectively. They allow you to acquire a lock and release it automatically.

    3) Start – stop
    - Context managers also help you to work with a scenario that requires the start and stop phases.
    - For example, you can use a context manager to start a timer and stop it automatically.

    4) Change – reset
    - Context managers can work with change and reset scenario.
    - For example, your application needs to connect to multiple data sources. And it has a default connection.
    - To connect to another data source:

        + First, use a context manager to change the default connection to a new one.
        + Second, work with the new connection
        + Third, reset it back to the default connection once you complete working with the new connection.



Implementing Python context manager protocol

"""


# The following shows a simple implementation of the open() function using the context manager protocol:
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print(f"Opening the file {self.filename}.")
        self.__file = open(self.filename, self.mode)
        return self.__file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f"Closing the file {self.filename}.")
        if not self.__file.closed:
            self.__file.close()

        return False


with File(".\\playground\\data.txt", "r") as f:
    print(int(next(f)))

# Opening the file .\playground\data.txt.
# 100
# Closing the file .\playground\data.txt.


"""
How it works.
    + First, initialize the filename and mode in the __init__() method.
    + Second, open the file in the __enter__() method and return the file object.
    + Third, close the file if it’s open in the __exit__() method.
"""
