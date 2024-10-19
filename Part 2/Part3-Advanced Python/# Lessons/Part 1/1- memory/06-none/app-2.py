"""
The applications of the Python None object

"""

# 1) Using Python None as an initial value for a variable
# When a variable doesn’t have any meaningful initial value, you can assign None to it, like this:
state = None


# Then you can check if the variable is assigned a value or not by checking it with None as follows:
if state is None:
    state = "start"

print(state)  # start
