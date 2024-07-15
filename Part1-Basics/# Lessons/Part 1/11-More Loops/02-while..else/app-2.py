"""
while else

"""


# The following shows the new version of the program that uses the while else statement:

basket = [
    {"fruit": "apple", "qty": 20},
    {"fruit": "banana", "qty": 30},
    {"fruit": "orange", "qty": 10},
]

fruit = input("Enter a fruit:")

index = 0

while index < len(basket):
    item = basket[index]
    # check the fruit name
    if item["fruit"] == fruit:
        print(f"The basket has {item['qty']} {item['fruit']}(s)")
        found_it = True
        break

    index += 1
else:
    qty = int(input(f"Enter the qty for {fruit}:"))
    basket.append({"fruit": fruit, "qty": qty})
    print(basket)


""" 
    In this program, the else clause replaces the need of having the found_it flag and the if statement after the loop.

    If the fruit is not found, the while loop is terminated normally and the else clause will be executed to add a new fruit to the list.

    However, if the fruit is found, the while loop will be encountered the break statement and terminated prematurely. In this case, the else clause won’t be executed.

"""
