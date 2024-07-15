"""
REPLACE
- The replace() method returns a copy of a string with some or all matches of a substring replaced with a new substring.

- The following shows the syntax of the replace() method:

    str.replace(substr, new_substr [, count])

- The replace() method accepts three parameters:

    substr is a string that is to be replaced by the new_substr.
    new_substr is the string that replaces the substr
    count is an integer that specifies the first count number of occurrences of the substr that will be replaced with the new_substr. The count parameter is optional. If you omit the count argument, the replace() method will replace all the occurrences of the substr by the new_substr.

- It’s important to note that the replace() method returns a copy of the original string with some or all occurrences of the substr replaced by the new_substr. It doesn’t change the original string.

"""

# 1) Replacing all occurrences of a substring with a new substring
# The following example uses the string replace() method to replace all occurrences of the substring 'We' by the new substring 'Python':

s = "We will, We will rock you!"
new_s = s.replace("We", "Python")

print(s)
print(new_s)  # Python will, Python will rock you!


# 2) Replacing some occurrences of a substring by a new substring
# The following example uses the replace() method to replace the first occurrence of the substring 'bye' by the new substring 'baby':
s = "Baby bye bye bye!"
new_s = s.replace("bye", "baby", 1)

print(new_s)  # Baby baby bye bye!
# In this example, we passed the count argument as one. Therefore, the replace() method just replaces the first occurrence of the string 'bye' with the string 'baby'
