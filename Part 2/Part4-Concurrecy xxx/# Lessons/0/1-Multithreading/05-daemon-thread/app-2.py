"""
DAEMON THREADS


"""


# Now, let’s turn the thread into a daemon thread:

from threading import Thread
import time


def show_timer():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f"Has been waiting for {count} second(s)...")


t = Thread(target=show_timer, daemon=True)  # Daemon Thread
t.start()

answer = input("Do you want to exit?\n")


"""
If you run the program, input something, and hit enter, the program will terminate. For example:

    Do you want to exit?
    Has been waiting for 1 second(s)...
    Y
    
The program terminates because it doesn’t need to wait for the daemon thread to complete. Also, the daemon thread is killed automatically when the program exits
"""

"""
Daemon threads vs. non-daemon threads

- The following table illustrates the differences between daemon and non-daemon threads:

                        Daemon Threads                          Non-daemon Threads
    Thread creation	    t = Thread(target=f, daemon=True)	    t = Thread(target=f)
    The program needs to wait before exiting        No	        Yes
    Kind of tasks	    Not critical like logging	            Critical

\\\\\\\\\\\\\\\\\

Summary

    A daemon thread is a background thread.
    A daemon thread is useful for executing tasks that are not critical.
    The program can exit and doesn’t need to wait for the daemon threads to be completed.
    A daemon thread is automatically killed when the program exits.
"""
