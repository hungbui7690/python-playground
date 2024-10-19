"""
Passing arguments to threads

"""

# The following program shows how to pass arguments to the function assigned to a thread:

from time import sleep, perf_counter
from threading import Thread


# First, define a task() function that accepts an argument:
def task(id):
    print(f"Starting the task {id}...")
    sleep(1)
    print(f"The task {id} completed")


start_time = perf_counter()


# Second, create 10 new threads and pass an id to each. The threads list is used to keep track of all newly created threads:
threads = []
for n in range(1, 11):
    t = Thread(target=task, args=(n,))
    threads.append(t)
    t.start()


# Notice that if you call the join() method inside the loop, the program will wait for the first thread to complete before starting the next one.
# Third, wait for all threads to complete by calling the join() method:
for t in threads:
    t.join()

end_time = perf_counter()

print(f"It took {end_time- start_time: 0.2f} second(s) to complete.")


"""
Starting the task 1...
Starting the task 2...
Starting the task 3...
Starting the task 4...
Starting the task 5...
Starting the task 6...
Starting the task 7...
Starting the task 8...
Starting the task 9...
Starting the task 10...
The task 3 completed
The task 4 completed
The task 1 completed
The task 8 completed
The task 7 completed
The task 2 completed
The task 9 completed
The task 5 completed
The task 6 completed
The task 10 completed
It took  1.02 second(s) to complete.
"""


# Notice that the program doesn’t execute the thread in the order from 1 to 10.
