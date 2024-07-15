"""
do…while Loop Statement Emulation
- Unlike the while loop, the do...while loop statement executes at least one iteration. It checks the condition at the end of each iteration and executes a code block until the condition is False.

- The following shows the pseudo code for the do...while loop in Python:

    do
        # code block
    while condition

- Unfortunately, Python doesn’t support the do...while loop. However, you can use the while loop and a break statement to emulate the do...while loop statement.

    while True:
        # code block

        # break out of the loop
        if condition
            break

"""

# Suppose that you need to develop a number guessing game with the following logic:
# First, generate a random number within a range e.g., 0 to 10.
# Then, repeatedly prompt users for entering a number. If the entered number is lower or higher than the random number, give users a hint. If the entered number equals the random number, the loop stops.
from random import randint

# determine the range
MIN = 0
MAX = 10

# generate a secret number
secret_number = randint(MIN, MAX)

# initialize the attempt
attempt = 0

# The first attempt
input_number = int(input(f"Enter a number between {MIN} and {MAX}:"))
attempt += 1

if input_number > secret_number:
    print("It should be smaller.")
elif input_number < secret_number:
    print("It should be bigger.")
else:
    print(f"Bingo! {attempt} attempt(s)")

# From the second attempt
while input_number != secret_number:
    input_number = int(input(f"Enter a number between {MIN} and {MAX}:"))
    attempt += 1

    if input_number > secret_number:
        print("It should be smaller.")
    elif input_number < secret_number:
        print("It should be bigger.")
    else:
        print(f"Bingo! {attempt} attempt(s)")


# Since the while loop checks for the condition at the beginning of each iteration, it’s necessary to repeat the code that prompts for user input and checking the number twice, one before the loop and one inside the loop.
