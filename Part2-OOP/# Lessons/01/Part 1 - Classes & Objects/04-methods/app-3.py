"""
Python Methods
- By definition, a method is a function that is bound to an instance of a class. This tutorial helps you understand how it works under the hood.

"""


# The following redefines the Request class where the send function accepts a list of arguments:
class Request:
    def send(*args):
        print("Sent", args)


http_request = Request()


# The following calls the send function from the Request class:
Request.send()  # Sent ()


# The send() function doesn’t receive any arguments.
# However, if you call the send() function from an instance of the Request class, the args is not empty:
http_request.send()
# Sent (<__main__.Request object at 0x000001B36E29F2D0>,)
# In this case, the send() method receives an object which is the http_request, which is the object that it is bound to.


# The following illustrates that the object that calls the send() method is the one that Python implicitly passes into the method as the first argument:
print(hex(id(http_request)))  # 0x19ab9d8f2d0
http_request.send()  # Sent (<__main__.Request object at 0x0000019AB9D8F2D0>,)

# The http_request object is the same as the one Python passes to the send() method as the first argument because they have the same memory address. In other words, you can access the instance of the class as the first argument inside the send() method:


# The following method call:
http_request.send()

# is equivalent to the following function call:
Request.send(http_request)


# For this reason, a method of an object always has the object as the first argument. By convention, it is called self:
class RequestX:
    def send(self):
        print("Sent", self)


# If you have worked with other programming languages such as Java or C#, the self is the same as the this object.


"""
    Summary

    - When you define a function inside a class, it’s purely a function. However, when you call the function via an instance of a class, the function becomes a method. Therefore, a method is a function that is bound to an instance of a class.
    - A method is an instance of the method class.
    - A method has the first argument (self) as the object to which it is bound.
    - Python automatically passes the bound object to the method as the first argument. By convention, its name is self.
"""
