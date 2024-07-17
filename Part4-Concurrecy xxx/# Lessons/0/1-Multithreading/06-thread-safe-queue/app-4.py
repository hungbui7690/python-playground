"""
Marking a task as completed

- An item that you add to the queue represents a unit of work or a task.

- When a thread calls the get() method to get the item from the queue, it may need to process it before the task is considered completed.

        item = queue.get()
        # process the item
        # ...
        # mark the item as completed
        queue.task_done()

\\\\\\\\\\\\\\\\\\\\\

Waiting for all tasks on the queue to be completed

- To wait for all tasks on the queue to be completed, you can call the join() method on the queue object:

        queue.join()

"""

# The following example illustrates how to use the thread-safe queue to exchange data between two threads:

import time
from queue import Empty, Queue
from threading import Thread


# First, define the producer() function that adds numbers from 1 to 11 to the queue. It delays one second in each iteration:
def producer(queue):
    for i in range(1, 6):
        print(f"Inserting item {i} into the queue")
        time.sleep(1)
        queue.put(i)


# Second, define the consumer() function that gets an item from the queue and processes it. It delays two seconds after processing each item on the queue:
def consumer(queue):
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f"Processing item {item}")
            time.sleep(2)

            # The queue.task_done() indicates that the function has processed the item on the queue.
            queue.task_done()


# Third, define the main() function that creates two threads, one thread adds a number to the queue every one second while another thread process an item on the queue every two seconds:
def main():
    # 1. Create a new queue by calling the Queue() constructor
    queue = Queue()

    # 2. Create a new thread called producer_thread and start it immediately
    producer_thread = Thread(target=producer, args=(queue,))
    producer_thread.start()

    # 3. Create a daemon thread called consumer_thread and start it immediately.
    consumer_thread = Thread(target=consumer, args=(queue,), daemon=True)
    consumer_thread.start()

    # 4. Wait for all the numbers to be added to the queue using the join() method of the thread.
    producer_thread.join()

    # 5. Wait for all the tasks on the queue to be completed by calling the join() method of the queue.
    queue.join()


if __name__ == "__main__":
    main()


# In this picture, the producer adds a number to the queue every second, and the consumer process a number from the queue every two seconds. It also displays the numbers on the queue every second.


"""
Summary
- Use the Queue class of the queue module to safely exchange data between multiple threads.

"""
