"""
if Statement

"""

age = input("Enter your age:")
if int(age) >= 18:
    print("You're eligible to vote.")
    print("Let's go and vote.")
# Enter your age:11


# If you don’t use the indentation correctly, the program will work differently. For example:
age = input("Enter your age:")
if int(age) >= 18:
    print("You're eligible to vote.")
print("Let's go and vote.")
# Enter your age:11
# Let's go and vote.
