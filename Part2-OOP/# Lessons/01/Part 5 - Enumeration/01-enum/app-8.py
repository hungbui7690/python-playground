"""
Python enumeration example

"""

from enum import Enum
import json


# The following example defines an enumeration called ResponseStatus:
class ResponseStatus(Enum):
    PENDING = "pending"
    FULFILLED = "fulfilled"
    REJECTED = "rejected"


# Suppose you receive a response from an HTTP request with the following string:
response = """{
    "status":"fulfilled"
}"""


# And you want to look up the ResponseStatus enumeration by the status. To do that, you need to convert the response’s string to a dictionary and get the value of the status:
data = json.loads(response)
status = data["status"]


# And then you look up the member of the ResponseStatus enumeration by the status’ value:
print(ResponseStatus(status))  # PromiseStatus.FULFILLED
