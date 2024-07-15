"""
FIND

- The find() is a string method that finds a substring in a string and returns the index of the substring.

- The following illustrates the syntax of the find() method:

        str.find(sub[, start[, end]])

- The find() method accepts three parameters:

    sub is the substring to look for in the str.
    start and end parameters are interpreted as in the slice str[start:end], which specifies where to search for the substring sub.

- Both start and end parameters are optional. The start parameter defaults to zero. And the end parameter defaults to the length-1 where length is the length of the str.

- If the str doesn’t contain the substring sub within the slice str[start:end], the find() method returns -1.

- In practice, you should use the find() method only if you want to know the position of the substring. If you just want to check whether a string contains a substring, you should use the in operator instead:

        sub in str


"""


# 1) Using the Python string find() method to find a substring in a string
# The following example shows how to use the find() method to find the substring 'Johny' in the string 'Johny Johny Yes Papa':

s = "Johny Johny Yes Papa"
result = s.find("Johny")

print(result)  # 0
# Because the string 'Johny Johny Yes Papa' has two substrings 'Johny', the find() method returns the index of the first occurrence of the substring 'Johny'.


# 2) Using the Python string find() method to find a substring in a string within a slice
# The following example uses the find() method to locate the substring 'Johny' in the string 'Johny Johny Yes Papa' within the slice str[1:]:

s = "Johny Johny Yes Papa"
result = s.find("Johny", 1)

print(result)  # 6
# In this example, the find() method returns the index of the second occurrence of the substring 'Johny' in the string 'Johny Johny Yes Papa'.


# 3) The substring doesn’t exist in the string example
# The following example returns -1 because the substring 'Julia' doesn’t exist in the string 'Johny Johny Yes Papa':

s = "Johny Johny Yes Papa"
result = s.find("Julia")

print(result)  # -1
