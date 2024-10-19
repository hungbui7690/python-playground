"""
Using Python threading to develop a multi-threaded program example

- To create a multi-threaded program, you need to use the Python "threading" module.

        from threading import Thread
        new_thread = Thread(target=fn,args=args_tuple)

- The Thread() accepts many parameters. The main ones are:

        + target: specifies a function (fn) to run in the new thread.
        + args: specifies the arguments of the function (fn). The args argument is a tuple.

"""

# First, import the Thread class from the threading module
from threading import Thread
from time import sleep, perf_counter


def task():
    print("Starting a task...")
    sleep(1)
    print("done")


start_time = perf_counter()

# Second, create a new thread by instantiating an instance of the Thread class
t1 = Thread(target=task)
t2 = Thread(target=task)

# Third, start the thread by calling the start() method of the Thread instance
t1.start()
t2.start()

# If you want to wait for the thread to complete in the main thread, you can call the join() method
# By calling the join() method, the main thread will wait for the second thread to complete before it is terminated.
t1.join()
t2.join()

end_time = perf_counter()

print(f"It took {end_time- start_time: 0.2f} second(s) to complete.")


# Starting a task...
# Starting a task...
# done
# done
# It took  1.00 second(s) to complete.


"""
When the program executes, it’ll have three threads: the main thread is created by the Python interpreter, and two threads are created by the program.

As shown clearly from the output, the program took one second instead of two to complete.

The following diagram shows how threads execute: pic-2
"""
