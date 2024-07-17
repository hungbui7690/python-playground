"""
Introduction to the Python regular expressions

- Regular expressions (called regex or regexp) specify search patterns. Typical examples of regular expressions are the patterns for matching email addresses, phone numbers, and credit card numbers.

- Regular expressions are essentially a specialized programming language embedded in Python. And you can interact with regular expressions via the built-in re module in Python. <pic-1>



- The following shows an example of a simple regular expression:

    '\d'

- In this example, a regular expression is a string that contains a search pattern. The '\d' is a digit character set that matches any single digit from 0 to 9.

** Note that you’ll learn how to construct more complex and advanced patterns in the next tutorials. This tutorial focuses on the functions that deal with regular expressions.

"""

# First, import the re module:
import re


# Second, compile the regular expression into a Pattern object:
p = re.compile("\d")


# Third, use one of the methods of the Pattern object to match a string:
s = "Python 3.10 was released on October 04, 2021"
result = p.findall(s)


# The findall() method returns a list of single digits in the string s.
print(result)  # ['3', '1', '0', '0', '4', '2', '0', '2', '1']


"""
Besides the findall() method, the Pattern object has other essential methods that allow you to match a string:

    Method	    Purpose
    match()	    Find the pattern at the beginning of a string
    search()	  Return the first match of a pattern in a string
    findall()	  Return all matches of a pattern in a string
    finditer()	Return all matches of a pattern as an iterator

"""
