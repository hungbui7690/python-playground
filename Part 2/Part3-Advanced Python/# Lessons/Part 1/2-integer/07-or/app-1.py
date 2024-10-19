"""
or Operator
- The or operator is a logical operator. Typically, you use the or operator to combine two Boolean expressions and return a Boolean value.

- The or operator returns True if one of the two operands is True. And it returns False only if both operands are False.

"""

# The following example shows how to use the or operator:
is_admin = False
is_editor = True
can_edit = is_admin or is_editor

print(can_edit)  # True
