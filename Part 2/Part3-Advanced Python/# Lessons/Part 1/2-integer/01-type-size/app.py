"""
INTEGERS
- Integers are whole numbers that include negative numbers, zero, and positive numbers such as -3, -2, -1, 0, 1, 2, 3.

- Python uses the class int to represent all integer numbers. All integers are objects.

\\\\\\\\\\\\\\\\\\\\\\\

How computers store integers

- Computers can’t store integers directly. Instead, they only can store binary numbers such as 0 and 1.
- To store integers, the computers need to use binary numbers to represent the integers.
- For example, to store the number 5, the computers need to represent it using a base-2 number. As you can see, it takes 3 bits to store the number 5 in the memory.

- Suppose that you have 8 bits, you can store up to 255 integers from zero to 255.
- By using 8 bits, you can store up to 28 – 1 = 255 integers.
- To store both negative integers, zero, and positive integers, you need to reserve 1 bit for storing the sign, negative (-) and positive (+). Therefore, with 8 bits:

    The largest integer that the computers can represent is 27 = 127.
    And the computers can store all integers in the range (-127, 127)

- Because the number zero doesn’t have a sign, the computers can squeeze out an extra number. Therefore, 8 bits can store all integers from -128 to 127.

\\\\\\\\\\\\\\\\\\\\\\\

How Python represents integers

- Other programming languages such as Java and C# use a fixed number of bits to store integers.
- For example, C# has the int type that uses 32-bits and the long type that uses 64 bits to represent integers. Based on the integer types, you can determine the ranges of the integers those types can represent.
- Python, however, doesn’t use a fixed number of bit to store integers. Instead, Python uses a variable number of bits to store integers. For example, 8 bits, 16 bits, 32 bits, 64 bits, 128 bits, and so on.
- The maximum integer number that Python can represent depends on the memory available.
- Also, integers are objects. Python needs an extra fixed number of bytes as an overhead for each integer.
- It’s important to note that the bigger the integer numbers are, the slower the calculations such as +, -, … will be.

"""

from sys import getsizeof

# The following defines a variable that references an integer and uses the type() function to get the class name of the integer:
counter = 10
print(type(counter))  # <class 'int'>
# As you can see clearly from the output, an integer is an instance of the class int.


# To get the size of an integer, you use the getsizeof() function of the sys module.
# The getsizeof() function returns the number of bytes that Python uses to represent an integer. For example:
counter = 0
size = getsizeof(counter)
print(size)  # 28 bytes

# To store the number 0, Python uses 24 bytes. Since storing the number zero, Python needs to use only 1 bit. Note that 1 byte equals 8 bits.
# Therefore, you can think that Python uses 24 bytes as an overhead for storing an integer object.


counter = 100
size = getsizeof(counter)
print(size)  # 28 bytes
# It returns 28 bytes. Since 24 bytes is an overhead, Python uses 4 bytes to represent the number 100.


# The following shows the size of the integer 264 :
counter = 2**64
size = getsizeof(counter)
print(size)  # 36 bytes
