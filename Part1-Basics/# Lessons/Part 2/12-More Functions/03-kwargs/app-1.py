"""
Introduction to the Python **kwargs parameters

- In Python, a function can have a parameter preceded by two stars (**). For example: **kwargs

- The **kwargs is called a keyword parameter.

- When a function has the **kwargs parameter, it can accept a variable number of keyword arguments as a dictionary.

- The two stars (**) are important. However, the name kwargs is by convention. Therefore, you can use any other meaningful names such as **configs and **files.

"""


# The following example defines a function called connect() that accepts a **kwargs parameter:
def connect(**kwargs):
    print(type(kwargs))
    print(kwargs)


# The following function call shows an empty dictionary to the screen:
connect()  # <class 'dict'> + {}
# In this example, we didn’t pass any arguments to the connect() function, the kwargs is empty dictionary.


# The following calls the connect() function and passes some keyword arguments into it:
connect(server="localhost", port=3306, user="root", password="Py1hon!Xt")
# {'server': 'localhost', 'port': 3306, 'user': 'root', 'password': 'Py1hon!Xt'}
