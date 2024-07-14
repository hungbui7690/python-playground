"""
\\\\\\\\\\\\\\\\\\\\\\\\\
Function
- using the "def" keyword

\\\\\\\\\\\\\\\\\\\\\\\\\
What is a function
- A function is a named code block that performs a job or returns a value.

\\\\\\\\\\\\\\\\\\\\\\\\\
Why do you need functions in Python
- Sometimes, you need to perform a task multiple times in a program. And you don’t want to copy the code for that same task all over places.

- To do so, you wrap the code in a function and use this function to perform the task whenever you need it.

- For example, whenever you want to display a value on the screen, you need to call the print() function. Behind the scene, Python runs the code inside the print() function to display a value on the screen.

- In practice, you use functions to divide a large program into smaller and more manageable parts. The functions will make your program easier to develop, read, test, and maintain.

- The print() function is one of many built-in functions in Python. It means that these functions are available everywhere in the program.

"""


# Here’s a simple function that shows a greeting:
def greet():
    """Display a greeting to users"""
    print("Hi")


"""
    This example shows the simplest structure of a function. A function has two main parts: a function definition and body.

    1) Function definition

        A function definition starts with the def keyword and the name of the function (greet).

        If the function needs some information to do its job, you need to specify it inside the parentheses (). The greet function in this example doesn’t need any information, so its parentheses are empty.

        The function definition always ends in a colon (:).

    2) Function body

        All the indented lines that follow the function definition make up the function’s body.

        The text string surrounded by triple quotes is called a docstring. It describes what the function does. Python uses the docstring to generate documentation for the function automatically.

        The line print('Hi') is the only line of actual code in the function body. The greet() function does one task: print('Hi').

\\\\\\\\\\\\\\\\\\\\\\\\

    Calling a function

        When you want to use a function, you need to call it. A function call instructs Python to execute the code inside the function.

        To call a function, you write the function’s name, followed by the information that the function needs in parentheses.
"""

# The following example calls the greet() function. Since the greet() function doesn’t need any information, you need to specify empty parentheses like this:
greet()  # Hi
