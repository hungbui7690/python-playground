"""
Using Lock to prevent the race condition

- To prevent race conditions, you can use the Lock class from the threading module. A lock has two states: locked and unlocked.

    First, create an instance the Lock class:

          lock = Lock()

    By default, the lock has the unlocked status until you acquire it.

    Second, acquire a lock by calling the acquire() method:

          lock.acquire()

    Third, release the lock once the thread completes changing the shared variable:

          lock.release()

"""


# The following example shows how to use the Lock object to prevent the race condition in the previous program:

from threading import Thread, Lock
from time import sleep


counter = 0


# First, add a second parameter to the increase() function.
def increase(by, lock):
    global counter

    # Third, acquire a lock before accessing the counter variable and release it after updating the new value.
    lock.acquire()

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f"counter={counter}")

    lock.release()


# Second, create an instance of the Lock class.
lock = Lock()

# create threads
t1 = Thread(target=increase, args=(10, lock))
t2 = Thread(target=increase, args=(20, lock))

# start the threads
t1.start()
t2.start()


# wait for the threads to complete
t1.join()
t2.join()


print(f"The final counter is {counter}")


# counter=10
# counter=30
# The final counter is 30


"""
Summary

    A race condition occurs when two threads access a shared variable at the same time.
    Use a Lock object to prevent the race condition
    Call the acquire() method of a lock object to acquire a lock.
    Call the release() method of a lock object to release the previously acquired lock.
"""
