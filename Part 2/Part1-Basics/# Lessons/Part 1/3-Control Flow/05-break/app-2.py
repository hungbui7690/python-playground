"""
while condition:
    # more code
    if condition:
        break

"""

# It’ll prompt you for entering your favorite color. The program will stop once you enter quit:
print("-- Help: type quit to exit --")
while True:
    color = input("Enter your favorite color:")
    if color.lower() == "quit":
        break

"""

    How it works.

        The while True creates an indefinite loop.
        Once you enter quit, the condition color.lower() == 'quit' evaluates True that executes the break statement to terminate the loop.
        The color.lower() returns the color in lowercase so that you can enter Quit, QUIT or quit to exit the program.

"""
