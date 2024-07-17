"""
THREADING


"""


# Single-threaded applications

# First, import the sleep() and perf_counter() functions from the time module:
from time import sleep, perf_counter


# Second, define a function that takes one second to complete:
def task():
    print("Starting a task...")
    sleep(1)
    print("done")


# Third, get the value of the performance counter by calling the perf_counter() function:
start_time = perf_counter()


# Fourth, call the task() function twice:
task()
task()


# Fifth, get the value of the performance counter by calling the perf_counter() function:
end_time = perf_counter()


# Finally, output the time that takes to complete running the task() function twice:
print(f"It took {end_time- start_time: 0.2f} second(s) to complete.")

"""
Starting a task...
done
Starting a task...
done
It took  2.00 second(s) to complete.


- As you may expect, the program takes about two seconds to complete. If you call the task() function 10 times, it would take about 10 seconds to complete.
- The following diagram illustrates how the program works: pic-1
- First, the task() function executes and sleeps for one second. Then it executes the second time and also sleeps for another second. Finally, the program completes.
- When the task() function calls the sleep() function, the CPU is idle. In other words, the CPU doesn’t do anything, which is not efficient in terms of resource utilization.
- This program has one process with a single thread, which is called the main thread. Because the program has only one thread, it’s called the single-threaded program.

"""
