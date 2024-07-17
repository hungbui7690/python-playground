"""
Apply Multi Threading

"""


# The following program has the same functionality. However, it uses multiple threads instead:

from threading import Thread
from time import perf_counter


def replace(filename, substr, new_substr):
    print(f"Processing the file {filename}")
    # get the contents of the file
    with open(filename, "r") as f:
        content = f.read()

    # replace the substr by new_substr
    content = content.replace(substr, new_substr)

    # write data into the file
    with open(filename, "w") as f:
        f.write(content)


def main():
    filenames = [
        ".\\playground\\data\\test1.txt",
        ".\\playground\\data\\test2.txt",
        ".\\playground\\data\\test3.txt",
        ".\\playground\\data\\test4.txt",
        ".\\playground\\data\\test5.txt",
        ".\\playground\\data\\test6.txt",
        ".\\playground\\data\\test7.txt",
        ".\\playground\\data\\test8.txt",
        ".\\playground\\data\\test9.txt",
        ".\\playground\\data\\test10.txt",
    ]

    # create threads
    threads = [
        Thread(target=replace, args=(filename, "Hello World ", "XYZ "))
        for filename in filenames
    ]

    # start the threads
    for thread in threads:
        thread.start()

    # wait for the threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f"It took {end_time- start_time :0.2f} second(s) to complete.")


"""
Processing the file .\playground\data\test1.txt
    ...
    ...
Processing the file .\playground\data\test10.txt
It took 0.01 second(s) to complete.

\\\\\\\\\\\\\\\\\\

Summary

    Use the Python threading module to create a multi-threaded application.
    Use the Thread(function, args) to create a new thread.
    Call the start() method of the Thread class to start the thread.
    Call the join() method of the Thread class to wait for the thread to complete in the main thread.
    Only use threading for I/O bound processing applications.

"""
