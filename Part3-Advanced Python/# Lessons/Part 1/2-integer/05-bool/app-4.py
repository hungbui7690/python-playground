"""
The __len__() method

- If the class of the object doesn’t have the __bool__() method, Python will return the result of __len__() method.

- If the result of the __len__() method is zero, the bool() returns False. Otherwise, it returns True.

- That’s why an empty list is always False while a list with at least one element is True.

"""


# Suppose that you have a function that returns a list or None. The result list can have zero or more elements:
def get_list():
    pass


# To display the elements of the list, you may come up with the following code:
my_list = get_list()

if my_list is not None and len(my_list) > 0:
    for element in my_list:
        print(element)
else:
    print("List is None or empty")
# The condition in the if clause makes sure that my_list is not None or empty.


# However, this condition is unnecessary because you can shorten it like this. The code works the same:
my_list = get_list()

if my_list:
    for element in my_list:
        print(element)
else:
    print("List is None or empty")

# In this case, if the my_list is None or empty, then Python evaluates it to False.
# Finally, if a class that doesn’t have both __bool__() and __len__() methods, the instances of that class always evaluate to True.


# Summary
# Python uses the bool class to represent boolean values: True and False.
# True and False are instances of the bool class. In fact, they’re singleton objects of the bool class.
# Every object has a boolean value, which can be True or False. The bool(object) returns the Boolean value of the obj.
# Under the hood the bool() returns a Boolean value by calling the __bool__() or __len__() method of the object. If both methods don’t exist, the bool() returns True.
