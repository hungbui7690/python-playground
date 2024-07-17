"""
DAEMON THREADS

\\\\\\\\\\\\\\\\\\\

Introduction to the Python daemon threads

- In Python, every program has at least one thread called the main thread. To create a program that has more than one thread, you use the threading module. By using multiple threads, you can execute tasks concurrently.

- Sometimes, you may want to execute a task in the background. To do that you use a special kind of thread called a daemon thread.

- By definition, daemon threads are background threads. In other words, daemon threads execute tasks in the background.

- Daemon threads are helpful for executing tasks that support non-daemon threads in the program. For example:

    Log information to a file in the background.
    Scrap contents from a website in the background.
    Auto-save the data into a database in the background.


\\\\\\\\\\\\\\\\\\

Creating a daemon thread

- To create a daemon thread, you set the daemon to True in the Thread constructor:

    t = Thread(target=f, deamon=True)

- Alternatively, you can set the daemon property to True after creating the Thread‘s instance:

    t = Thread(target=f)
    t.deamon = True

"""


# The following example shows how to create a non-daemon thread that shows the number of seconds that the program has been waiting for:

from threading import Thread
import time


# First, define a function show_timer() that displays the number of seconds that the program has been waiting for.
def show_timer():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f"Has been waiting for {count} second(s)...")


# Second, create a new thread that executes the show_timer() function:
t = Thread(target=show_timer)

# Third, start the thread:
t.start()

# Finally, call the input() function to prompt users for input:
answer = input("Do you want to exit?\n")


"""
If you run the program, it’ll show the following output and run forever.

    Do you want to exit?Has been waiting for 1 second(s)...
    Has been waiting for 2 second(s)...
    Has been waiting for 3 second(s)...
    Has been waiting for 4 second(s)...
    Y
    Has been waiting for 5 second(s)...
    Has been waiting for 6 second(s)...


To terminate the program, you need to kill the terminal.

The program runs indefinitely because the thread t is a non-daemon thread. The program needs to wait for all non-daemon threads to complete before it can exit.

"""
