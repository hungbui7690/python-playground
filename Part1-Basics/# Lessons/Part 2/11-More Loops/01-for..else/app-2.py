"""
for else


"""


# The following shows the new version of the program that uses the for else statement:

people = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 22},
    {"name": "Peter", "age": 30},
    {"name": "Jenifer", "age": 28},
]

name = input("Enter a name:")

for person in people:
    if person["name"] == name:
        print(person)
        break
else:
    print(f"{name} not found!")

"""
    By using the for else statement, the program doesn’t need to use a flag and an if statement after the loop.

    In this new program, if the input name matches a person on the list, it’ll show the person’s information and exit the loop by using the break statement.

    When the loop encounters the break statement, the else clause won’t execute.
"""
