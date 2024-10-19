"""
The Python or operator is short-circuiting

- When evaluating an expression that involves the or operator, Python can sometimes determine the result without evaluating all the operands. This is called short-circuit evaluation or lazy evaluation.

- If x is truthy, then the or operator returns x. Otherwise, it returns y.

- In other words, if x is truthy, then the or operator doesn’t need to evaluate y. It just returns x immediately. This is why the evaluation is called lazy or short-circuiting evaluation.

- The or operator only evaluates y and returns the result of the evaluation if x is falsy.

- In Python, every object associates with a Boolean value. And the x and y can be any object.

\\\\\\\\\\\\\\\\\\\

Setting a default value for a variable

- The or operator allows you to set a default value for a variable, for example:

      var_name = value or default

"""

# The following example prompts you for input. If you don’t enter anything, the lang will default to 'Python':
lang = input("Enter your language:") or "Python"
print(lang)


# The following example defines a function get_data() that returns a list of numbers. It uses the built-in min() function to find the lowest element in the list:
def get_data(args=None):
    if args:
        return [1, 2, 3]
    return []


lowest = min(get_data(args=True))
print(lowest)  # 1

lowest = min(get_data() or [0])
print(lowest)  # 0

# In this example, if the get_data() function returns an empty list, the or operator will treat its result as a falsy value.
# Since the first operand is falsy, the or operator needs to evaluate the second operand [0]. In this case, you can specify the default minimum value in the second operand.
