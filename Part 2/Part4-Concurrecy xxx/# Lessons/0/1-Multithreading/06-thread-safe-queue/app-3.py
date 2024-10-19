"""
Getting the size of the queue


"""

from queue import Queue


queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)


# The qsize() method returns the number of items in the queue:
size = queue.qsize()
print(size)  # 3


# Also, the empty() method returns True if the queue is empty or False otherwise. On the other hand, the full() method returns True if the queue is full or False otherwise.
is_empty = queue.empty()
print(is_empty)  # False
