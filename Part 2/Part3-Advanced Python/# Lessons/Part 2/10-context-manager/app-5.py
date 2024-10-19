"""
Python context manager protocol

- Python context managers work based on the context manager protocol.
- The context manager protocol has the following methods:

    __enter__() – setup the context and optionally return some object
    __exit__() – cleanup the object.

- If you want a class to support the context manager protocol, you need to implement these two methods.
- Suppose that ContextManager is a class that supports the context manager protocol.

- The following shows how to use the ContextManager class:

        with ContextManager() as ctx:
            # do something
        # done with the context

- When you use ContextManager class with the with statement, Python implicitly creates an instance of the ContextManager class (instance) and automatically call __enter__() method on that instance.
- The __enter__() method may optionally return an object. If so, Python assigns the returned object the ctx.
- Notice that ctx references the object returned by the __enter__() method. It doesn’t reference the instance of the ContextManager class.
- If an exception occurs inside the with block or after the with block, Python calls the __exit__() method on the instance object.

    pic

- Functionally, the with statement is equivalent to the following try...finally statement:

        instance = ContextManager()
        ctx = instance.__enter__()

        try:
            # do something with the txt
        finally:
            # done with the context
            instance.__exit__()


The __enter__() method

    - In the __enter__() method, you can carry the necessary steps to setup the context.
    - Optionally, you can returns an object from the __enter__() method.


The __exit__() method

    - Python always executes the __exit__() method even if an exception occurs in the with block.
    - The __exit__() method accepts three arguments: exception type, exception value, and traceback object. - All of these arguments will be None if no exception occurs.

            def __exit__(self, ex_type, ex_value, ex_traceback):
                ...
    - The __exit__() method returns a boolean value, either True or False.
    - If the return value is True, Python will make any exception silent. Otherwise, it doesn’t silence the exception.


"""
