"""
Get Item from a Queue


"""

from queue import Queue


queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)


# Getting an item from the queue
# The get() method will block until an item is available for retrieval from the queue.
item = queue.get()
print(item)  # 1


# To get an item from the queue without blocking, you can set the block parameter to False:
try:
    item = queue.get(block=False)
    print(item)  # 2
except queue.Empty as e:
    print(e)


# To get an item from the queue and block with a time limit, you can use the get() method with a timeout:
try:
    item = queue.get(timeout=10)
    print(item)  # 3
except queue.Empty as e:
    print(e)
