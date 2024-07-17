"""
STOP A THREAD

\\\\\\\\\\\\\\\\\\\

Introduction to the Event object

To stop a thread, you use the Event class of the threading module. The Event class has an internal thread-safe boolean flag that can be set to True or False. By default, the internal flag is False.

In the Event class, the set() method sets the internal flag to True while the clear() method resets the flag to False. Also, the is_set() method returns True if the internal flag is set to True.

To stop a child thread from the main thread, you use an Event object with the following steps:

    First, create a new Event object and pass it to a child thread.
    Second, periodically check if the internal flag of the Event object is set in the child thread by calling the is_set() method and stop the child thread if the internal flag was set.
    Third, call the set() method in the main thread at some point in time to stop the child thread.

The following flow chart illustrates the above steps: pic-1


"""

from threading import Thread, Event
from time import sleep


# The task() function uses an Event object and returns None. It will be executed in a child thread:
# The task() function iterates over the numbers from 1 to 5. In each iteration, we use the sleep() function to delay the execution and exit the loop if the internal flag of the event object is set.
def task(event: Event) -> None:
    for i in range(6):
        print(f"Running #{i+1}")
        sleep(1)
        if event.is_set():
            print("The thread was stopped prematurely.")
            break
    else:
        print("The thread was stopped maturely.")


def main() -> None:
    event = Event()  # First, create a new Event object:

    # Next, create a new thread that executes the task() function with an argument as the Event object:
    thread = Thread(target=task, args=(event,))

    # Then, start executing the child thread:
    thread.start()

    # After that, suspend the main thread for three seconds:
    sleep(3)

    # Finally, set the internal flag of the Event object to True by calling the set() method. This will also stop the child thread:
    event.set()


if __name__ == "__main__":
    main()


# Running #1
# Running #2
# Running #3
# The thread was stopped prematurely.
