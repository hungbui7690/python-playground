"""
F-STRINGS
- Python 3.6 introduced the f-strings that allow you to format text strings faster and more elegant.
- The f-strings provide a way to embed variables and expressions inside a string literal using a clearer syntax than the format() method.

"""

name = "John"
s = f"Hello, {name}!"
print(s)  # Hello, John!


"""
    How it works.

        First, define a variable with the value 'John'.
        Then, place the name variable inside the curly braces {} in the literal string. Note that you need to prefix the string with the letter f to indicate that it is an f-string. It’s also valid if you use the letter in uppercase (F).
        Third, print out the string s.

    It’s important to note that Python evaluates the expressions in f-string at runtime. It replaces the expressions inside an f-string with their values.

"""
