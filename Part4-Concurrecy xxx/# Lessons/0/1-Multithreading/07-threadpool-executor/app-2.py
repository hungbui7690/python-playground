"""
Using the map() method example

"""

# The following program uses a ThreadPoolExecutor class. However, instead of using the submit() method, it uses the map() method to execute a function:

from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor


def task(id):
    print(f"Starting the task {id}...")
    sleep(1)
    return f"Done with task {id}"


start = perf_counter()

with ThreadPoolExecutor() as executor:
    # First, call the map() method of the executor object to run the task function for each id in the list [1,2]. The map() method returns an iterator that contains the result of the function calls.
    results = executor.map(task, [1, 2])

    # Second, iterate over the results and print them out:
    for result in results:
        print(result)

finish = perf_counter()

print(f"It took {finish-start} second(s) to finish.")


"""
Starting the task 1...
Starting the task 2...
Done with task 1
Done with task 2
It took 1.003100199974142 second(s) to finish.
"""
