"""
- Sometimes, you want to terminate a for loop or a while loop prematurely regardless of the results of the conditional tests. In these cases, you can use the break statement:

    break

- The following shows how to use the break statement inside a for loop:

    for index in range(n):
        # more code here
        if condition:
            break

"""

# This example shows how to use the break statement inside a for loop:
for index in range(0, 10):
    print(index)
    if index == 3:
        break
# 0 1 2 3


# When you use the break statement in a nested loop, it’ll terminate the innermost loop. For example:
for x in range(5):
    for y in range(5):
        # terminate the innermost loop
        if y > 1:
            break
        # show coordinates on the screen
        print(f"({x},{y})")
# This example uses two for loops to show the coordinates from (0,0) to (5,5) on the screen.
# The break statement in the nested loop terminates the innermost loop when the y is greater than one.
