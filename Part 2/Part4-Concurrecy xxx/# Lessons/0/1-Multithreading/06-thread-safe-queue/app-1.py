"""
THREAD-SAFE QUEUE
- The built-in queue module allows you to exchange data safely between multiple threads. The Queue class in the queue module implements all required locking semantics.

\\\\\\\\\\\\\

Create a Queue

"""

from queue import Queue


# To create a new queue, you use the Queue constructor as follows:
queue = Queue()


# To create a queue with a size limit, you can use the maxsize parameter. For example, the following creates a queue that can store up to 10 items:
queue = Queue(maxsize=1)


# Adding an item to the queue
queue.put(1)
# Once the queue is full, you cannot add an item to the queue. The call to the put() method will block until the queue has space available.


# If you don’t want the put() method to block if the queue is full, you can set the block argument to False:
# In this case, the put() method will raise the queue.Full exception if the queue is full:
# try:
#     queue.put(2, block=False)
# except AttributeError as e:
#     print(e)
# queue.Full


# To add an item to a sized limited queue and block with a timeout, you can use the timeout parameter like this:
queue = Queue(maxsize=10)
try:
    queue.put("x", timeout=3)
except queue.Full as e:
    print(e)
