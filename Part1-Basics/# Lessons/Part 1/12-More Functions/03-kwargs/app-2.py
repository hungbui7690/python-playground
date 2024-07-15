"""
Introduction to the Python **kwargs parameters

"""


# Inside the connect() function, you can use the kwargs argument as a dictionary.
# If you want to pass a dictionary to the function, you need to add two stars (**) to the argument like this:


def connect(**kwargs):
    print(kwargs)


config = {
    "server": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Py1thon!Xt12",
}

connect(**config)
# {'server': 'localhost', 'port': 3306, 'user': 'root', 'password': 'Py1thon!Xt12'}
