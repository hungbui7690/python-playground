"""
Logical Operators
- and
- or
- not

"""

# The following example uses the and operator to combine two conditions that compare the price with numbers:
price = 9.99
print(price > 9 and price < 10)  # True

# The following example shows how to use the or operator:
print(price > 10 or price < 20)  # True

# The following example uses the not operator. Since the price > 10 returns False, the not price > 10 returns True:
print(not price > 10)  # True

# Here is another example that combines the not and the and operators:
print(not (price > 5 and price < 10))  # False

"""
  The following shows the precedence of the not, and, and or operators:

    Operator	Precedence
    not	      High
    and	      Medium
    or	      Low

  In case an expression has several logical operators with the same precedence, Python will evaluate them from the left to right:

    a or b and c	        means	    a or (b and c)
    a and b or c and d	  means	    (a and b) or (c and d)
    a and b and c or d	  means	    ((a and b) and c) or d
    not a and b or c	    means	    ((not a) and b) or c

"""
