"""
Backslash in raw strings

"""

# Raw strings treat the backslash character (\) as a literal character. The following example treats the backslash character \ as a literal character, not a special character:

s = r"\n"
print(s)  # \n


"""
    Summary

        The python backslash character (\) is a special character used as a part of a special sequence such as \t and \n.
        Use the Python backslash (\) to escape other special characters in a string.
        F-strings cannot contain the backslash a part of expression inside the curly braces {}.
        Raw strings treat the backslash (\) as a literal character.

"""
