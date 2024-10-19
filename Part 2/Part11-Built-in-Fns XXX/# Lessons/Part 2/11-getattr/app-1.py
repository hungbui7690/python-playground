"""
getattr
- The getattr() function allows you to get the value of the named attribute of an object. Here’s the syntax of the getattr() function:

    getattr(object, name[, default])

- The getattr() function accepts three parameters:

    object is the object from which you want to get the value of a named attribute.
    name is a string that specifies the attribute name of the object.
    default: if the named attribute doesn’t exist in the object, the getattr() function returns the default. If you omit the default and the named attribute doesn’t exist, the function will raise an AttributeError exception.


"""


# The following example illustrates how to use the getattr() to get the attribute values of an object:
class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email


member = Member("John Doe", "john@pythontutorial.net")


# use the getattr() function to get the values of the name and email attribute:
name = getattr(member, "name")
print(name)  # 👉 John Doe

email = getattr(member, "email")
print(email)  # 👉 john@pythontutorial.net

# It is the same as accessing the attributes directly:
print(member.name)  # 👉 John Doe
print(member.email)  # 👉 john@pythontutorial.net


# Attempt to access the non-existing attribute age. It’ll raise an AttributeError exception.
# age = getattr(member, "age")
# print(age)  # 🛑 AttributeError


# To avoid the exception, you can pass None as the default value like this:
age = getattr(member, "age", None)
print(age)
# In this case, the age is None.
