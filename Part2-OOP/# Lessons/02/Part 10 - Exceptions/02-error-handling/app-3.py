"""
Except order example

- When you catch an exception in the except clause, you need to place the exceptions from most specific to the least specific in terms of exception hierarchy.

- The following shows three exception classes: Exception, LookupError, and IndexError: pic

- If you catch the exception, you need to place them in the following order: IndexError, LookupErorr, and Exception.

"""

# For example, the following defines a list of three strings and attempts to access the 4th element:
colors = ["red", "green", "blue"]

try:
    print(colors[3])
except IndexError as e:
    print(type(e), "Index error")
except LookupError as e:
    print(type(e), "Lookup error")

# <class 'IndexError'> Index error


# The colors[3] access causes an IndexError exception. However, if you swap the except clauses and catch the LookupError first and the IndexError second like this:
try:
    print(colors[3])
except LookupError as e:
    print(type(e), "Lookup error")
except IndexError as e:
    print(type(e), "Index error")

# <class 'IndexError'> Lookup error


# The exception is still IndexError but the following message is misleading.
