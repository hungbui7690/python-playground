"""
Python Methods

"""


# The following defines a Request class that contains a function send():
class Request:
    def send():
        print("Sent")


# The following creates a new instance of the Request class:
http_request = Request()


# If you display the http_request.send, it’ll return a bound method object:
print(http_request.send)
# <bound method Request.send of <__main__.Request object at 0x000001782C85F2D0>>


# So the http_request.send is not a function like Request.send. The following checks if the Request.send is the same object as http_request.send. It’ll returns False as expected:
print(type(Request.send) is type(http_request.send))  # False
print(type(Request.send))  # <class 'function'>
print(type(http_request.send))  # <class 'method'>


# The reason is that the type of the Request.send is function while the type of the http_request.send is method, as shown below:
print(type(http_request.send))  # <class 'method'>
print(type(Request.send))  # <class 'function'>


# So when you define a function inside a class, it’s purely a function. However, when you access that function via an object, the function becomes a method.
# Therefore, a method is a function that is bound to an instance of a class.
# If you call the send() function via the http_request object, you’ll get a TypeError as follows:
# TypeError: Request.send() takes 0 positional arguments but 1 was given
# http_request.send()
# Because the http_request.send is a method that is bound to the http_request object, Python always implicitly passes the object to the method as the first argument.
