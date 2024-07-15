"""
for else
- In Python, the for statement can have an optional else clause, which you may not be familiar with especially if you’re coming from other languages such as Java or C#.

- The following shows the syntax of the for statement with the else clause:

    for item in iterables:
        # process item
    else:
        # statement

- In this syntax, the else clause will execute only if the loop runs normally. In other words, the else clause won’t execute if the loop encounters a break statement.
- In addition, the else clause also executes when the iterables object has no item.

"""


# Suppose that you have a list of people, where each person is a dictionary that consists of name and age like this:

people = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 22},
    {"name": "Peter", "age": 30},
    {"name": "Jenifer", "age": 28},
]

# And you want to search for a person by name.
# If the list contains the person, you want to display the information of that person. Otherwise, you want to show a message saying that the name is not found.

name = input("Enter a name:")

found = False
for person in people:
    if person["name"] == name:
        found = True
        print(person)
        break

if not found:
    print(f"{name} not found!")


"""
    How it works:

        First, prompt for a name by using the input() function.
        Then, set a flag (found) to False. If the input name matches with a person on the list, set its value to True, show the person’s information and exit the loop by using the break statement.
        Finally, check the found flag and show a message.


    The following runs a program with the name Peter and Maria:
    - 1st run:

        Enter a name:Peter
        {'name': 'Peter', 'age': 30}

    - 2nd run:

        Enter a name:Maria
        Maria not found!
    

    It works perfectly fine.
    However, if you use the for else statement, the program will be much shorter.

"""
