"""
Using a static type checker tool: mypy

- Python doesn’t have an official static type checker tool. At the moment, the most popular third-party tool is Mypy. Since Mypy is a third-party package, you need to install it using the following pip command:

    ~~ pip install mypy

- Once installed mypy, you can use it to check the type before running the program by using the following command:

    ~~ mypy app.py


"""


def say_hi(name: str) -> str:
    return f"Hi {name}"


greeting = say_hi(123)
print(greeting)  # Hi 123
