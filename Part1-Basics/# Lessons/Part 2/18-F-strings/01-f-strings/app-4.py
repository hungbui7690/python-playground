"""
Curly braces

- When evaluating an f-string, Python replaces double curly braces with a single curly brace. However, the doubled curly braces do not signify the start of an expression.

"""

# Python will not evaluate the expression inside the double curly brace and replace the double curly braces with a single one. For example:
s = f"{{1+2}}"
print(s)  # {1+2}


# The following shows an f-string with triple curly braces:
s = f"{{{1+2}}}"
print(s)  # {3}
# In this example, Python evaluates the {1+2} as an expression, which returns 3. Also, it replaces the remaining doubled curly braces with a single one.


# To add more curly braces to the result string, you use more than triple curly braces:
s = f"{{{{1+2}}}}"
print(s)  # {{1+2}}
# In this example, Python replaces each pair of doubled curly braces with a single curly brace.
