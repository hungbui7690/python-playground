"""
Python Exceptions



"""

# The program runs the same if you use the Exception class instead of the LookupError class:

colors = ["red", "green", "blue"]

try:
    print(colors[3])
except Exception as e:
    print(e.__class__, "-", e)

print("Continue to run")

# <class 'IndexError'> - list index out of range
# Continue to run

# In practice, you should catch the exceptions as specific as possible so that you know how to deal with each exception in a specific way.
