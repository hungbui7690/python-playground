"""
PYTHON THREADING EVENT

\\\\\\\\\\\\\\\\\\\\\\\

Introduction to the Python threading Event object

- Sometimes, you need to communicate between the threads. To do it, you can use a mutual exclusion lock (mutex) and a boolean variable.
- However, Python provides you with a better way to communicate between threads using the Event class from the threading module.

- The Event class offers a simple but effective way to coordinate between threads: one thread signals an event while other threads wait for it.
- The Event object wraps a boolean flag that can be set (True) or unset (False). Threads that share an Event object can check if the event is set, set the event, unset the event, or wait for the event to be set.

\\\\\\\\\\\\\\\\\\\\

Let’s see how the Event object works.

- First, import the Event from the threading module:

    from threading import Event

- Next, create a new Event object:

    event = Event()

- By default, the event is not set. The is_set() method of the event object will return False:

    if event.is_set():
    # ...

- Then, set an event using the set() method:

    event.set()

- Once an event is set, all the threads that wait on the event will be notified automatically.
- After that, unset an event via the clear() method:

    event.clear()

- Finally, threads can wait for the event to be set via the wait() method:

    event.wait()

- The wait() method blocks the execution of a thread until the event is set. In other words, the wait() method will block the current thread until another thread call the set() method to set the event.
- If an event is set, the wait() function returns immediately.
- To specify how long the thread is going to wait, you can use the timeout argument. For example:

    event.wait(timeout=5) # wait for 5 seconds

"""

# The following example shows a simple example of using the Event object to communicate between threads:

from threading import Thread, Event
from time import sleep


# First, define the task() function that accepts an Event object and an integer:
def task(event: Event, id: int) -> None:
    print(f"Thread {id} started. Waiting for the signal....")

    # Inside, the task() function, we call the wait() method of the event object to wait for the event to be set by the main thread.
    event.wait()
    print(f"Received signal. The thread {id} was completed.")


# Second, create an Event object inside the main() function:
def main() -> None:
    event = Event()

    # Third, create two child threads that execute the task() function with the same event object and different id 1 and 2:
    t1 = Thread(target=task, args=(event, 1))
    t2 = Thread(target=task, args=(event, 2))

    # Fourth, start both threads by calling the start() method:
    t1.start()
    t2.start()

    print("Blocking the main thread for 3 seconds...")

    # Fifth, call the sleep() method to block the main thread for three seconds:
    # Since the task() function call the wait() method of the event object, both t1 and t2 threads will wait for the event to be set before continuing.
    sleep(3)

    # Finally, set the event by calling the set() method from the main thread:
    # Both t1 and t2 threads will be notified and continue executing until the end.
    event.set()


if __name__ == "__main__":
    main()


"""
Thread 1 started. Waiting for the signal....
Thread 2 started. Waiting for the signal....
Blocking the main thread for 3 seconds...
Received signal. The thread 1 was completed.
Received signal. The thread 2 was completed.
"""


# Summary
# Use the threading.Event class to communicate between threads.
# Use the set() method to set the event and clear() method to unset the event.
# Use the is_set() method to check if an event is set.
# Use the wait() method to wait for the event to be set.
