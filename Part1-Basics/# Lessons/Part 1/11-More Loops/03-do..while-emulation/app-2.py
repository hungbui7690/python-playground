"""
do…while Loop Statement Emulation

"""

# To avoid this duplicate code, you can use a while loop to emulate do while loop as follows:

from random import randint

# determine the range
MIN = 0
MAX = 10

# generate a secret number
secret_number = randint(MIN, MAX)

# initialize the attempt
attempt = 0

while True:
    attempt += 1

    input_number = int(input(f"Enter a number between {MIN} and {MAX}:"))

    if input_number > secret_number:
        print("It should be smaller.")
    elif input_number < secret_number:
        print("It should be bigger.")
    else:
        print(f"Bingo! {attempt} attempt(s)")
        break
