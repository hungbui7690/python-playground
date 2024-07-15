"""
while else
- In Python, the while statement may have an optional else clause:

    while condition:
        # code block to run
    else:
        # else clause code block

"""


# Suppose that we have the following list of fruits where each fruit is a dictionary that consists of the fruit name and qty keys:

basket = [
    {"fruit": "apple", "qty": 20},
    {"fruit": "banana", "qty": 30},
    {"fruit": "orange", "qty": 10},
]

# We want to make a program that allows the users to enter a fruit name. Based on the input name, we’ll search for it from the basket list and show its quantity if the fruit is on the list.
# In case the fruit is not found, we’ll allow users to enter the quantity for that fruit and add it to the list.

fruit = input("Enter a fruit:")

index = 0
found_it = False

while index < len(basket):
    item = basket[index]
    # check the fruit name
    if item["fruit"] == fruit:
        found_it = True
        print(f"The basket has {item['qty']} {item['fruit']}(s)")
        break

    index += 1

if not found_it:
    qty = int(input(f"Enter the qty for {fruit}:"))
    basket.append({"fruit": fruit, "qty": qty})
    print(basket)


"""
    Note that there’s better way to develop this program. The program in this example is solely for the demonstration purpose.

    How it works:

        First, prompt for an user input by using the input() function.
        Second, initialize the index to zero and found_it flag to False. The index will be used for accessing the list by index. And the found_it flag will be set to True if the fruit name will be found.
        Third, iterate over the list and check if the fruit name matched with the input name. If yes, set the found_it flag to True, show the fruit’s quantity, and exit the loop by using the break statement.
        Finally, check the found_it flag after the loop and add the new fruit to the list if the found_it is False.



    The following runs the program when apple is the input:

        Enter a fruit:apple
        The basket has 20 apple(s)

    And the following runs the program when lemon is the input:

        Enter a fruit:lemon
        Enter the qty for lemon:15
        [{'fruit': 'apple', 'qty': 20}, {'fruit': 'banana', 'qty': 30}, {'fruit': 'orange', 'qty': 10}, {'fruit': 'lemon', 'qty': 15}]

    The program works as expected.
    However, it’ll be more concise if you use the while else statement instead.

"""
