"""
Python slice type

- Everything in Python is an object including the slice. A slice is actually an object of the slice type. When you use the slicing notation:

      seq[start:stop]

"""

# The start:stop is a slice object.
# slice(start, stop)
s = slice(1, 3)

print(type(s))  # <class 'slice'>
print(s.start, s.stop)  # 1 3


# So instead of using the slicing notation:
colors = ["red", "green", "blue", "orange"]

colors[1:3]

# … you can use the slice object instead:
s = slice(1, 3)
print(colors[s])  # ['green', 'blue']
