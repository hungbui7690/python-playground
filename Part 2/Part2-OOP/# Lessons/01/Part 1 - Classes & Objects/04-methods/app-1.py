"""
Python Methods
- By definition, a method is a function that is bound to an instance of a class. This tutorial helps you understand how it works under the hood.

"""


# The following defines a Request class that contains a function send():
class Request:
    def send():
        print("Sent")


# And you can call the send() function via the Request class like this:
Request.send()  # Sent


# The send() is a function object, which is an instance of the function class as shown in the following output:
print(Request.send)  # <function Request.send at 0x000001AA64858EA0>


# The type of the send is function:
print(type(Request.send))  # <class 'function'>
