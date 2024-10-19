"""
Python Modulo
- Python uses the percent sign (%) as the modulo operator. The modulo operator always satisfies the following equation:

      N = D * ( N // D) + (N % D)

- In this equation:

    N is the numerator.
    D is the denominator.
    // is the floor division operator
    And % is the modulo operator

- If both N and D are positive integers, the modulo operator returns the remainder of N / D. However, it is not the case for the negative numbers. Therefore, you should always stick with the above equation.

"""

# The following example illustrates how to use the modulo operator (%) with positive integers:
a = 16
b = 5

m = a % b
f = a // b

print(f"{a} % {b} = {m}")  # 16 % 5 = 1
print(f"{a} // {b} = {f}")  # 16 // 5 = 3


# The following shows how to use the modulo operator (%) with negative integers:
a = -16
b = 5

m = a % b
f = a // b

print(f"{a} % {b} = {m}")  # 4
print(f"{a} // {b} = {f}")  # -4
