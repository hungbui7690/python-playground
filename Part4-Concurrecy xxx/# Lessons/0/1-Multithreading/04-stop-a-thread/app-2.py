"""
Stopping a thread that uses a child class of the Thread class


"""
# The following example shows how to create a child thread using a derived class of the Thread class and uses the Event object to stop the child thread from the main thread in demand:

# To stop the thread that uses a derived class of the Thread class, you also use the Event object of the threading module.
from threading import Thread, Event
from time import sleep


class Worker(Thread):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event

    def run(self) -> None:
        for i in range(6):
            print(f"Running #{i+1}")
            sleep(1)
            if self.event.is_set():
                print("The thread was stopped prematurely.")
                break
        else:
            print("The thread was stopped maturely.")


def main() -> None:
    # create a new Event object
    event = Event()

    # create a new Worker thread
    thread = Worker(event)

    # start the thread
    thread.start()

    # suspend  the thread after 3 seconds
    sleep(3)

    # stop the child thread
    event.set()


if __name__ == "__main__":
    main()


"""
Running #1
Running #2
Running #3
The thread was stopped prematurely.
"""

"""
How it works.

    First, define a Worker class that extends the Thread class from the threading module. The __init__() method of the Worker class accepts an Event object.

    Second, override the run() method of the Worker class and use the event object to stop the thread.

    Third, define the main() function that creates an event, a Worker thread, and passes the event object 
    to the Worker thread. The remaining logic is the same as the main() function in the previous example.

\\\\\\\\\\\\\\\\\\
    
Summary

    Use the Event object to stop a child thread.
    Use the set() method to set an internal flag of an Event object to True.
    Use the is_set() method to check if the internal flag of an Event object was set.
"""
