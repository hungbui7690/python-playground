"""
\\\\\\\\\\\\\\\\\\\\\\
Type Conversion

"""

# 1) To get input from users, you use the input() function. For example:
value = input("Enter a value:")
print(value)
# the input() function returns a string, not an integer.


# 2) The following example prompts you to enter two input values: net price and tax rate. After that, it calculates the tax and displays the result on the screen:
# price = input("Enter the price ($):")
# tax = input("Enter the tax rate (%):")

# tax_amount = (
#     price * tax / 100
# )  # error: TypeError: can't multiply sequence by non-int of type 'str'

# print(f"The tax amount price is ${tax_amount}")
"""
- Since the input values are strings, you cannot apply the multiply operator.
- To solve this issue, you need to convert the strings to numbers before performing calculations.
- To convert a string to a number, you use the int() function. More precisely, the int() function converts a string to an integer.
"""

# 3) The following example uses the int() function to convert the input strings to numbers:
price = input("Enter the price ($):")
tax = input("Enter the tax rate (%):")

tax_amount = int(price) * int(tax) / 100
print(f"The tax amount is ${tax_amount}")


"""
  Other type conversion functions
  - Besides the int(str) functions, Python supports other type conversion functions. The following shows the most important ones for now:

      float(str) – convert a string to a floating-point number.
      bool(val) – convert a value to a boolean value, either True or False.
      str(val) – return the string representation of a value.

"""
