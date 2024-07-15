"""
Python enumeration example

"""

from enum import Enum
import json


# What if the status is not one of the values of the ResponseStatus members? then you’ll get an error. For example:
class ResponseStatus(Enum):
    PENDING = "pending"
    FULFILLED = "fulfilled"
    REJECTED = "rejected"


response = """{
    "status":"ok"
}"""

data = json.loads(response)
status = data["status"]


# 1. Error
# print(ResponseStatus(status))  # ValueError: 'ok' is not a valid ResponseStatus


# 2. Catch the error
try:
    if ResponseStatus(status) is ResponseStatus.FULFILLED:
        print("The request completed successfully")
except ValueError as error:
    print(error)


"""
Summary

    An enumeration is a set of members that have associated unique constant values.
    Create a new enumeration by defining a class that inherits from the Enum type of the enum module.
    The members have the same types as the enumeration to which they belong.
    Use the enumeration[member_name] to access a member by its name and enumeration(member_value) to access a member by its value.
    Enumerations are iterable.
    Enumeration members are hashable.
    Enumerable are immutable.
    Cannot inherits from an enumeration unless it has no members.
"""
