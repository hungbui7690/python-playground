"""
Python float class
- pic
  > Python can only use approximate float representations for those numbers.

"""

# The float() returns a floating-point number based on a number or a string. For example:
float(0.1)
float("1.25")
# If you pass an object (obj) to the float(obj), it’ll delegate to the obj.__float__(). If the __float__() is not defined, it’ll fall back to __index__().
# If you don’t pass any argument to the float(), it’ll return 0.0


# When you use the print() function, you’ll see that the number 0.1 is represented as 0.1 exactly.
# Internally, Python can only represent 0.1 approximately.
# To see how Python represents the 0.1 internally, you can use the format() function.
# The following shows how Python represents the number 0.1 using 20 digits:
print(format(0.1, ".20f"))  # 0.10000000000000000555
# As you can see, 0.1 is not exactly 0.1 but 0.10000000000000000555...
# Because Python can represent some floats approximately, it will cause many problems when you compare two floating-point numbers.
