"""
for index in range(n):
    if condition:
        continue
    # more code here

while condition1:
    if condition2:
        continue
    # more code here
"""

# The following example shows how to use the for loop to display even numbers from 0 to 9:
for index in range(10):
    if index % 2:
        continue
    print(index)

"""
    How it works.

    - First, iterate over a range of numbers from 0 to 9 using a for loop with the range() function.
    - Second, if the index is an odd number, skip the current iteration and start a new one. Note that the index % 2 returns 1 if the index is an odd number and 0 if the index is an even number.

"""


# The following example shows how to use the continue statement to display odd numbers between 0 and 9 to the screen:
# print the odd numbers
counter = 0
while counter < 10:
    counter += 1
    if not counter % 2:
        continue
    print(counter)

"""
    How it works.
    
        First, define the counter variable with an initial value of zero
        Second, start the loop as long as the counter is less than 10.
        Third, inside the loop, increase the counter by one in each iteration. If the counter is an even number, skip the current iteration. Otherwise, display the counter to the screen.

    Summary

        Use the Python continue statement to skip the current iteration and start the next one.

"""
