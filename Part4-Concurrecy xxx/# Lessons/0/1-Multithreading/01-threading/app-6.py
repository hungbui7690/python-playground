"""
When to use Python threading

- As introduced in the process and thread tutorial, there’re two main tasks:

    I/O-bound tasks – the time spent on I/O is significantly more than the time spent on computation
    CPU-bound tasks – the time spent on computation is significantly higher than the time waiting for I/O.

- Python threading is optimized for I/O bound tasks. For example, requesting remote resources, connecting a database server, or reading and writing files.


- A Practical Python threading example

    + Suppose that you have a list of text files in a folder e.g., C:/temp/. And you want to replace a text with a new one in all the files.

"""


# The following single-threaded program shows how to replace a substring with the new one in the text files:

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

    for filename in filenames:
        replace(filename, "text ", "Hello World ")


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    print(f"It took {end_time- start_time :0.2f} second(s) to complete.")


"""
Processing the file .\playground\data\test1.txt
...
Processing the file .\playground\data\test10.txt
It took 0.02 second(s) to complete.
"""
