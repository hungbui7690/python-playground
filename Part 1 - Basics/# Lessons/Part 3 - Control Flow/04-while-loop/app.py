"""
while Loop

    while condition:
      body

"""

# The following example uses a while statement to show 5 numbers from 0 to 4 to the screen:
max = 5
counter = 0
while counter < max:
    print(counter)
    counter += 1


# The following example uses the while statement to prompt users for input and echo the command that you entered back. It’ll run as long as you don’t enter the quit command:
command = ""
while command.lower() != "quit":
    command = input(">")
    print(f"Echo: {command}")
# Note that the command.lower() returns the command in lowercase format. This allows you to enter the quit command such as quit, QUIT, or Quit.
