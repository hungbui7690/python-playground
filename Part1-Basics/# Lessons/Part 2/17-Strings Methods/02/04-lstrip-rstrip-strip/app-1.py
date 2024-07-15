"""
LSTRIP
- The lstrip() method returns a copy of a string with the leading characters removed.

- Here is the syntax of the lstrip() method:

    str.lstrip([chars])

- The lstrip() method accepts one optional argument chars.

- The chars argument is a string that determines a set of characters which the lstrip() method will remove from the copy of the str.

- If you don’t pass the chars argument or use None, the chars argument defaults to whitespace characters. In this case, the lstrip() method will remove the leading whitespace characters from the copy of the str.

- The following are whitespace characters in Python:

    ' ' – the space character
    \t – the tab character
    \n – the newline or linefeed character
    \r – the carriage return
    \x0b – the vertical tab. It can be also expressed as \v.
    \x0c – the form feed character that forces a printer to move the next sheet of paper. It’s also expressed as \f.

"""

# 1) Using the lstrip() method to remove the leading whitespace characters
# The following example illustrates how to the lstrip() method to return a copy of a string with the leading whitespace characters removed:
s = "\t Readability counts."
print(s)  #          Readability counts.
new_s = s.lstrip()
print(new_s)  # Readability counts.

# In this example, the string s contains leading whitespace characters including a space and tab characters.
# Since we didn’t pass any argument to the lstrip() method, it returned a copy of the string s with all the leading whitespace characters removed.


# 2) Using the Python string lstrip() method to remove the leading characters
# The following example uses the lstrip() method to convert a list of strings where each string may contain the leading $ or £ sign:
data = ["$1250", "£2300", "3000"]
amounts = [float(amount.lstrip("$£")) for amount in data]
print(amounts)  # [1250.0, 2300.0, 3000.0]


# Summary

# Use the Python string lstrip(chars) method to return a copy of a string with the leading characters removed.
# Use the lstrip() method without argument to return a copy of a string with the leading whitespace removed.
