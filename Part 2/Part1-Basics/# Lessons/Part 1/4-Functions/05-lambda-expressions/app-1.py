"""
Lambda Expressions

- Sometimes, you need to write a simple function that contains one expression. However, you need to use this function once. And it’ll unnecessary to define that function with the def keyword.

- That’s where the Python lambda expressions come into play.

\\\\\\\\\\\\\\\\\\\

What are Python lambda expressions

- Python lambda expressions allow you to define anonymous functions.

- Anonymous functions are functions without names. The anonymous functions are useful when you need to use them once.

- A lambda expression typically contains one or more arguments, but it can have only one expression.

- The following shows the lambda expression syntax:

        lambda parameters: expression

- It’s equivalent to the following function without the "anonymous" name:

        def anonymous(parameters):
            return expression

"""


# //////////////////////////
# 1) Functions that accept a function example
# The following defines a function called get_full_name() that format the full name from the first name and last name:
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


"""
The get_full_name() function accepts three arguments:

    - first_name
    - last_name
    - A function that will format the full name (formatter). In turn, the formatter function accepts two arguments first name and last name.

"""


# The following defines two functions that return a full name from the first name and last name in different formats:
def first_last(first_name, last_name):
    return f"{first_name} {last_name}"


def last_first(first_name, last_name):
    return f"{last_name}, {first_name}"


# And this shows you how to call the get_full_name() function by passing the first name, last name, and first_last / last_first functions:
full_name = get_full_name("John", "Doe", first_last)
print(full_name)  # John Doe

full_name = get_full_name("John", "Doe", last_first)
print(full_name)  #  Doe, John


# Instead of defining the first_last and last_first functions, you can use lambda expressions.
# For example, you can express the first_last function using the following lambda expression:
lambda first_name, last_name: f"{first_name} {last_name}"

# This lambda expression accepts two arguments and concatenates them into a formatted string in the order first_name, space, and last_name.
# And the following converts the last_first function using a lambda expression that returns the full name in the format: last name, space, and first name:
lambda first_name, last_name: f"{last_name} {first_name}"


# By using lambda expressions, you can call the get_full_name() function as follows:
def get_full_nameX(first_name, last_name, formatter):
    return formatter(first_name, last_name)


full_name = get_full_nameX(
    "John", "Doe", lambda first_name, last_name: f"{first_name} {last_name}"
)
print(full_name)

full_name = get_full_nameX(
    "John", "Doe", lambda first_name, last_name: f"{last_name} {first_name}"
)
print(full_name)
