"""
Rounding
- Rounding means making a number simpler but keeping its value close to its original value. For example, 89 rounded to the nearest ten is 90 because 89 is closer to 90 than to 80.

- To round a number in Python, you use the built-in round() function:

    round(number [, ndigits])

- The round() function rounds the number to the closest multiple of 10-ndigits.

- In other words, the round() function returns the number rounded to ndigits precision after the decimal point.

- If ndigits is omitted or None, the round() will return the nearest integer.

"""


#

print(round(1.25))  # 1


# However, if you pass ndigits as zero, the round() function returns a float 1.0: pic-1
print(round(1.25, 0))  # 1.0
# Since ndigits is zero, the round() function rounds the number 1.25 to the closet multiple of 10^-(0) = 1.


print(round(15.5, -1))  # 20.0
# Because ndigits is -1, the round() function rounds the number 15.5 to the closest multiple of 20 (10^-(-1)): pic-2
# Since 15.5 is situated between 10 and 20 (multiple of 10), it’s closer to 20. Therefore, the round() function returns 20.


# When you round a number situated in the middle of two numbers, Python cannot find the closest number.
# For example, if you round the number 1.25 with n is 1. There will be no closest number:
# In this case, Python uses the IEEE 754 standard for rounding, called the banker’s rounding.
# In the banker’s rounding, a number is rounded to the nearest value, with ties rounded to the nearest value with an even least significant digit.
# Generally, the least significant digit in a number is the rightmost digit.
# The banker’s rounding comes from the idea that statistically 50% sample of numbers are rounded up and 50% are rounded down.
print(round(1.25, 1))  # 1.2
# Because the least significant digit of 1.2 is 2, which is even:


print(round(1.35, 1))  # 1.4
# Python uses banker’s rounding but not rounding away from zero because it’s less biased.


"""
For example, if you average three numbers 1.5, 2.5, and 3.5, the rounding away from zero returns 3.0 while the banker’s rounding returns 2.66:
  Number	  Banker’s Rounding	    Rounding away from zero
  1.5	      2	                    2
  2.5	      2	                    3
  3.5	      4	                    4
  Average	  2.66666…	            3.0

"""
