"""
SLICING

Numpy array slicing on on-dimensional arrays

- NumPy arrays use brackets [] and : notations for slicing like lists. By using slices, you can select a range of elements in an array with the following syntax:

    [m:n]

- This slice selects elements starting with m and ending with n-1. Note that the nth element is not included. In fact, the slice m:n can be explicitly defined as:

    [m:n:1]

- The number 1 specifies that the slice selects every element between m and n.
- To select every two elements, you can use the following slice:

    [m:n:2]

- In general, the following expression selects every k element between m and n:

    [m:n:k]

- If k is negative, the slice returns elements in reversed order starting from m to n+1. The following table illustrates the slicing expressions:

    Slicing             Meaning
    a[m:n]	            Select elements with an index starting at m and ending at n-1.
    a[:] or a[0:-1]	    Select all elements in a given axis
    a[:n]	              Select elements starting with index 0 and up to element with index n-1
    a[m:]	              Select elements starting with index m and up to the last element
    a[m:-1]	            Select elements starting with index m and up to the last element
    a[m:n:k]	          Select elements with index m through n (exclusive), with an increment k
    a[::-1]	            Select all elements in reverse order

"""

import numpy as np

a = np.arange(0, 10)

print("a=", a)  # a= [0 1 2 3 4 5 6 7 8 9]
print("a[2:5]=", a[2:5])  # a[2:5]= [2 3 4]
print("a[:]=", a[:])  # a[:]= [0 1 2 3 4 5 6 7 8 9]
print("a[0:-1]=", a[0:-1])  # a[0:-1]= [0 1 2 3 4 5 6 7 8]
print("a[0:6]=", a[0:6])  # a[0:6]= [0 1 2 3 4 5]
print("a[7:]=", a[7:])  # a[7:]= [7 8 9]
print("a[5:-1]=", a[5:-1])  # a[5:-1]= [5 6 7 8]
print("a[0:5:2]=", a[0:5:2])  # a[0:5:2]= [0 2 4]
print("a[::-1]=", a[::-1])  # a[::-1]= [9 8 7 6 5 4 3 2 1 0]
