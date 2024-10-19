"""
Multiline f-strings

"""

# Python allows you to have multiline f-strings. To create a multiline f-string, you place the letter f in each line. For example:
name = "John"
website = "PythonTutorial.net"
message = f"Hello {name}. " f"You're learning Python at {website}."
print(message)  # Hello John. You're learning Python on PythonTutorial.net.


# fmt: off
# If you want to spread an f-string over multiple lines, you can use a backslash (\) to escape the return character like this:
name = "John"
website = "PythonTutorial.net"
message = f"Hello {name}. \
        " f"You're learning Python at {website}."
print(message) # Hello John.         You're learning Python at PythonTutorial.net.



# fmt: on
# The following example shows how to use triple quotes (""") with an f-string:
name = "John"
website = "PythonTutorial.net"
message = f"""Hello {name}.
You're learning Python at {website}."""
print(message)
# Hello John.
# You're learning Python at PythonTutorial.net.
