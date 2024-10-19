"""
try…except…else


"""


# 2) Using Python try…except…else and finally example

# The else clause executes right before the finally clause if no exception occurs in the try clause.
# The following example shows how to use the try...except...else...finally clause:

fruits = {"apple": 10, "orange": 20, "banana": 30}

key = None
while True:
    try:
        key = input("Enter a key to lookup:")
        fruit = fruits[key.lower()]
    except KeyError:
        print(f"Error! {key} does not exist.")
    except KeyboardInterrupt:
        break
    else:
        print(fruit)
    finally:
        print("Press Ctrl-C to exit.")


"""
    How it works.

        First, define the fruits dictionary that contains three elements.
        Second, use a while loop to repeatedly get inputs from users. It stops the loop until the users press Ctrl-C.
        Third, use the try...except...else...finally clause inside the while loop. We use the user input to find for the element in the dictionary.

    - If the key doesn’t exist, the KeyError exception occurs, the except clause will execute.
    - If users press Ctrl-C, the KeyboardInterrupt exception occurs that executes the break statement to terminate the loop.
    - If the key is found in the fruits dictionary, the program prints out the found element.
    - The finally clause always executes. It shows the reminder to the users that they should press Ctrl-C to exit.


    Summary
    - Use the Python try...except...else statement provides you with a way to control the flow of the program in case of exceptions.
    - The else clause executes if no exception occurs in the try clause.
    - If so, the else clause executes after the try clause and before the finally clause.

"""
