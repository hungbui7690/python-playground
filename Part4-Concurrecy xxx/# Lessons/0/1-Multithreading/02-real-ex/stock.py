import threading
import requests
from lxml import html


# Define a new class called Stock that inherits from the Thread class of the threading module.
class Stock(threading.Thread):
    # Then, implement the __init__() method that accepts a symbol and initializes the url instance variable based on the symbol:
    def __init__(self, symbol: str) -> None:
        super().__init__()

        self.symbol = symbol
        self.url = f"https://finance.yahoo.com/quote/{symbol}"
        self.price = None

    def run(self):
        # Make a request to the URL using the requests.get() method:
        response = requests.get(self.url)

        # If the request is successful, the HTTP status code is 200. In this case, we get the HTML contents from the response and pass it to the fromstring() function of the html module from the lxml package:
        if response.status_code == 200:
            # parse the HTML
            tree = html.fromstring(response.text)

            # get the price in text
            price_text = tree.xpath(
                '//*[@id="nimbus-app"]/section/section/section/article/section[1]/div[2]/div[1]/section/div/section[2]/div[1]/fin-streamer[1]/span/text()'
            )

            # Once getting the price as text, we remove the comma and convert it to a number:
            if price_text:
                try:
                    self.price = float(price_text[0].replace(",", ""))
                except ValueError:
                    self.price = None

    # Add the __str__() method that returns the string representation of the Stock object:
    def __str__(self):
        return f"{self.symbol}\t{self.price}"


# For example, if you pass the symbol GOOG to the __init__() method, the URL will be:
# https://finance.yahoo.com/quote/GOOG


"""
- Every element on a webpage can be selected using something called XPath.
- To get the XPath of an element using Google Chrome, you inspect the page, right-click the element, select copy, and Copy XPath.
- pic
- The XPath of the stock price at the time of writing this tutorial is as follows: 

    //*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]

- To get the text of the element, you append the text() at the end of the XPath:

    //*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()

- Notice that if Yahoo changes the page structure, you need to change the XPath accordingly. Otherwise, the program won’t work as expected:

    price_text = tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()')

"""
