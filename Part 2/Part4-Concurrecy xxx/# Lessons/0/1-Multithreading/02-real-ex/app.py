"""
MULTITHREADING EXAMPLE


Inheriting from the Thread class

- We’ll develop a multithreaded program that scraps the stock prices from the Yahoo Finance website.
- To do that, we’ll use two third-party packages:

    @@ requests – to get the contents of a webpage.
    @@ lxml – to select a specific element of an HTML document.

- Install the requests and lxml modules using the pip command:

    ~~ pip install request lxml

!! Check stock.py to get the xpath of the data


"""

# 1. Define a new class called Stock that inherits from the Thread class of the threading module. We’ll place the Stock class in stock.py module.

from stock import Stock

# 2. Initialize a list of symbols:
symbols = ["MSFT", "GOOGL", "AAPL", "META"]


# 3. Create a thread for each symbol, start it, and append the thread to the threads list:
threads = []
for symbol in symbols:
    t = Stock(symbol)
    t.start()
    threads.append(t)


# 4. Finally, wait for all the threads in the threads list to complete and print out the stock price:
for t in threads:
    t.join()
    print(t)
