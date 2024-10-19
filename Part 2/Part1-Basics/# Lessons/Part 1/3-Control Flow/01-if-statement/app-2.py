"""
if Statement

"""

# if..else
age = input("Enter your age:")
if int(age) >= 18:
    print("You're eligible to vote.")
else:
    print("You're not eligible to vote.")
# Enter your age:11
# You're not eligible to vote.


# if…elif…else statement
"""
- The if...elif...else statement checks each condition (if-condition, elif-condition1, elif-condition2, …) in the order that they appear in the statement until it finds the one that evaluates to True.
- When the if...elif...else statement finds one, it executes the statement that follows the condition and skips testing the remaining conditions.
- If no condition evaluates to True, the if...elif...else statement executes the statement in the else branch.
- Note that the else block is optional. If you omit it and no condition is True, the statement does nothing.

"""
age = input("Enter your age:")

your_age = int(age)  # convert the string to int

# determine the ticket price
if your_age < 5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18
print(f"You'll pay ${ticket_price} for the ticket")  # show the ticket price

"""
  - If the input age is less than 5, the ticket price will be $5.
  - If the input age is greater than or equal to 5 and less than 16, the ticket price is $10.
  - Otherwise, the ticket price is $18.
"""
