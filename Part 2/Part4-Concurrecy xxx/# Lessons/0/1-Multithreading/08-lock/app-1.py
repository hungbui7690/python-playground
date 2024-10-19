"""
Threading Lock to Prevent Race Conditions

- What is a race condition

    A race condition occurs when two threads try to access a shared variable simultaneously.

    The first thread reads the value from the shared variable. The second thread also reads the value from the same shared variable.

    Then both threads try to change the value of the shared variable. And they race to see which thread writes a value to the variable last.

    The value from the thread that writes to the shared variable last is preserved because it overwrites the value that the previous thread wrote.

"""


# The following example illustrates a race condition:

# First, import Thread class from the threading module and the sleep() function from the time module:
from threading import Thread
from time import sleep


# Second, define a global variable called counter whose value is zero:
counter = 0


# Third, define a function that increases the value of the counter variable by a number:
def increase(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f"counter={counter}")


# Fourth, create two threads. The first thread increases the counter by 10 while the second thread increases the counter by 20:
t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))


# start the threads
t1.start()
t2.start()


# Sixth, from the main thread, wait for the threads t1 and t2 to complete:
t1.join()
t2.join()


print(f"The final counter is {counter}")


# In this program, both threads try to modify the value of the counter variable at the same time. The value of the counter variable depends on which thread completes last.

# If the thread t1 completes before the thread t2, you’ll see the following output:
# # counter=10
# # counter=20
# # The counter is 20


# Otherwise, you’ll see the following output:
# # counter=20
# # counter=10
# # The final counter is 10
