"""
The rename argument of the namedtuple function

- The namedtuple function accepts the rename the keyword-only argument that allows you to rename invalid field names.

"""

from collections import namedtuple


# The following results in an error because the field name _radius starts with an underscore (_):
# Circle = namedtuple("Circle", "center_x, center_y, _radius")


# However, when you use the rename argument, the namedtuple function automatically renames the _radius to a valid field name. For example:
CircleX = namedtuple("CircleX", "center_x, center_y, _radius", rename=True)


# To find field names of a named tuple, you can use the _fields class property. For example:

print(CircleX._fields)  # ('center_x', 'center_y', '_2')

# In this example, the namedtuple function changes the _radius field to _2 automatically.
