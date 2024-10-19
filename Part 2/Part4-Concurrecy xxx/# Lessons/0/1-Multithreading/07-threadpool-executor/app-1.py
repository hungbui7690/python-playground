"""
THREADPOOL EXECUTOR

\\\\\\\\\\\\\\\\\\\\

Introduction to the Python ThreadPoolExecutor class

- In the multithreading tutorial, you learned how to manage multiple threads in a program using the Thread class of the threading module. The Thread class is useful when you want to create threads manually.

- However, manually managing threads is not efficient because creating and destroying many threads frequently are very expensive in terms of computational costs.

- Instead of doing so, you may want to reuse the threads if you expect to run many ad-hoc tasks in the program. A thread pool allows you to achieve this.

\\\\\\\\\\\\\\\\\\\\

Thread pool

- A thread pool is a pattern for achieving concurrency of execution in a program. A thread pool allows you to automatically manage a pool of threads efficiently: pic-1

- Each thread in the pool is called a worker thread or a worker. A thread pool allows you to reuse the worker threads once the tasks are completed. It also protects against unexpected failures such as exceptions.

- Typically, a thread pool allows you to configure the number of worker threads and provides a specific naming convention for each worker thread.

- To create a thread pool, you use the ThreadPoolExecutor class from the concurrent.futures module.
ThreadPoolExecutor

- The ThreadPoolExecutor class extends the Executor class and returns a Future object.

\\\\\\\\\\\\\\\\\\\\

Executor

- The Executor class has three methods to control the thread pool:

    + submit() – dispatch a function to be executed and return a Future object. The submit() method takes a function and executes it asynchronously.
    + map() – execute a function asynchronously for each element in an iterable.
    + shutdown() – shut down the executor.

- When you create a new instance of the ThreadPoolExecutor class, Python starts the Executor.

- Once completing working with the executor, you must explicitly call the shutdown() method to release the resource held by the executor. To avoid calling the shutdown() method explicitly, you can use the context manager.

\\\\\\\\\\\\\\\\\\\\

Future object

- A Future is an object that represents the eventual result of an asynchronous operation. The Future class has two useful methods:

    + result() – return the result of an asynchronous operation.
    + exception() – return the exception of an asynchronous operation in case an exception occurs.

"""

# The following program uses a single thread:

from time import sleep, perf_counter


# First, define the task() function that takes about one second to finish. The task() function calls the sleep() function to simulate a delay:
def task(id):
    print(f"Starting the task {id}...")
    sleep(1)
    return f"Done with task {id}"


# Second, call the task() function twice and print out the result. Before and after calling the task() function, we use the perf_counter() to measure the start and finish time:
start = perf_counter()

print(task(1))
print(task(2))

finish = perf_counter()


# Third, print out the time the program took to run:
print(f"It took {finish-start} second(s) to finish.")


"""
Starting the task 1...
Done with task 1
Starting the task 2...
Done with task 2
It took 2.0144479 second(s) to finish.
"""

# Because the task() function takes one second, calling it twice will take about 2 seconds.
