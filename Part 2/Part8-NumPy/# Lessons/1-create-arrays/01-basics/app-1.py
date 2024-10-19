"""
WHAT IS NUMPY

Introduction to NumPy

- NumPy stands for Numerical Python and is pronounced as /ˈnʌmpaɪ/. Numpy is a Python library that performs numerical calculations.
- NumPy is very fast because it is written in the C programming language.
- NumPy is built on linear algebra. It’s about matrices and vectors and performing the mathematical calculations on them.

- The key concept in NumPy is the NumPy array data type. A NumPy array may have one or more dimensions:

    One dimension arrays (1D) represent vectors.
    Two-dimensional arrays (2D) represent matrices.
    And higher dimensional arrays represent tensors.

- Unlike the built-in list type that can hold the elements of different types, the NumPy arrays allow only one data type for all elements. Therefore, we say that the NumPy array requires homogeneous data values.
- A NumPy array can contain either integer or float numbers, but not both at the same time. This restriction allows Numpy to speed up the linear algebra calculations.
- NumPy supports basic operations such as average, minimum, maximum, standard deviation, variance, and many more.
- After mastering NumPy, you’ll have a powerful tool for data analysis on numerical multi-dimensional data.

\\\\\\\\\\\\\\\\\

What is NumPy for

- NumPy is an important library for:

    Data Science
    Machine learning
    Signal and image processing
    Scientific and engineer computing

\\\\\\\\\\\\\\\\\

Install NumPy

- Since NumPy is a third-party package, you need to install it. To install NumPy, you use the following pip command:

  ~~ pip install numpy

- Once NumPy is installed successfully, you can import it to your program like this:

    import numpy

- By convention, we use an alias for the NumPy library as np. Note you can use any aliases. But it’s a good practice to follow the community convention so that others can understand your code more quickly:

    import numpy as np

- Once you reference the NumPy module, you can use its functions and classes like creating a new array.
- For example, the following creates a new NumPy array that contains three temperatures in celsius:

    tc = np.array([25.5, 28.1, 30.6])

- To convert these temperatures from celsius to Kelvin, you use the following:

    tk =  tc * 9 / 5 + 32
    print(tk)

- Output:

    [77.9 82.58 87.08]

- As you can see from the example, the calculation is much simpler than the following Python code:

    tk = [c*9/5 + 32 for c in tc]
    print(tk)

- Output:

    [77.9, 82.58, 87.08000000000001]

- And the NumPy calculation’s speed is much faster.

\\\\\\\\\\\\\\\\\\

Summary

    NumPy stands for Numerical Python. It’s a Python library for numerical calculation.
    Use np as the alias for the NumPy module.

"""

import numpy as np

tc = np.array([25.5, 28.1, 30.6])

tk = [c * 9 / 5 + 32 for c in tc]
print(tk)
# [np.float64(77.9), np.float64(82.58), np.float64(87.08000000000001)]
