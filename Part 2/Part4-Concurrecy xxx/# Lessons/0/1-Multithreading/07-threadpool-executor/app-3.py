"""
Python ThreadPoolExecutor practical example
- The following program downloads multiple images from Wikipedia using a thread pool

"""

from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
import time
import os


# First, define a function download_image() that downloads an image from an URL and saves it into a file:
def download_image(url):
    image_data = None

    # The download_image() function the urlopen() function from the urllib.request module to download an image from an URL.
    with urlopen(url) as f:
        image_data = f.read()

    if not image_data:
        raise Exception(f"Error: could not download the image from {url}")

    filename = os.path.basename(url)
    with open(filename, "wb") as image_file:
        image_file.write(image_data)
        print(f"{filename} was downloaded...")


start = time.perf_counter()


urls = [
    "https://upload.wikimedia.org/wikipedia/commons/9/9d/Python_bivittatus_1701.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/4/48/Python_Regius.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/d/d3/Baby_carpet_python_caudal_luring.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/f/f0/Rock_python_pratik.JPG",
    "https://upload.wikimedia.org/wikipedia/commons/0/07/Dulip_Wilpattu_Python1.jpg",
]


# Second, execute the download_image() function using a thread pool by calling the map() method of the ThreadPoolExecutor object:
with ThreadPoolExecutor() as executor:
    executor.map(download_image, urls)


finish = time.perf_counter()


print(f"It took {finish-start} second(s) to finish.")


"""
Run the program

    Python_Regius.jpg was downloaded...
    Python_bivittatus_1701.jpg was downloaded...
    Rock_python_pratik.JPG was downloaded...
    Baby_carpet_python_caudal_luring.jpg was downloaded...
    Dulip_Wilpattu_Python1.jpg was downloaded...
    It took 1.4957328999880701 second(s) to finish.

Files will be downloaded


Summary

    A thread pool is a pattern for managing multiple threads efficiently.
    Use ThreadPoolExecutor class to manage a thread pool in Python.
    Call the submit() method of the ThreadPoolExecutor to submit a task to the thread pool for execution. The submit() method returns a Future object.
    Call the map() method of the ThreadPoolExecutor class to execute a function in a thread pool with each element in a list.
"""
