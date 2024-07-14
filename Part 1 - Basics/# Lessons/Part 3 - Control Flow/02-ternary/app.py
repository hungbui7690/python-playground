"""
Ternary Operator

"""

# if..else
age = input("Enter your age:")

if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5

print(f"The ticket price is {ticket_price}")
# Enter your age:18
# The ticket price is $20


# To make it more concise, you can use an alternative syntax like this:
ticket_price = 20 if int(age) >= 18 else 5
print(f"The ticket price is {ticket_price}")
