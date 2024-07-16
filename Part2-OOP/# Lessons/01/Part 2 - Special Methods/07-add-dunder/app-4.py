"""
Overloading inplace operators

- Some operators have the inplace version. For example, the inplace version of + is +=.

- For the immutable type like a tuple, a string, a number, the inplace operators perform calculations and don’t assign the result back to the input object.

- For the mutable type, the inplace operator performs the updates on the original objects directly. The assignment is not necessary.

- Python also provides you with a list of special methods that allows you to overload the inplace operator:

        Operator	Special Method
        +=	        __iadd__(self, other)
        -=	        __isub__(self, other)
        *=	        __imul__(self, other)
        /=	        __itruediv__(self, other)
        //=	        __ifloordiv__(self, other)
        %=	        __imod__(self, other)
        **=	        __ipow__(self, other)
        >>=	        __irshift__(self, other)
        <<=	        __ilshift__(self, other)
        &=	        __iand__(self, other)
        |=	        __ior__(self, other)
        ^=	        __ixor__(self, other)

- Let’s take an example of overloading the += operator.

- Suppose you have a cart object and you want to add an item to the cart. To do, you can define an add() method to the Cart class and use it like this:

    cart.add(item)

- Alternatively, you can implement the += operator in the Cart class. It allows you to add an item to the cart as follows:

    cart += item

- To support the += operator, you need to implement the __iadd__ special method in the Cart class.

"""


# First, define the Item class that has three attributes name, quantity, and price. Also, it has an amount property that returns the subtotal of the item:
class Item:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    @property
    def amount(self):
        return self.qty * self.price

    def __str__(self):
        return f"{self.name} {self.qty} ${self.price} ${self.amount}"


# Second, define the Cart class that implements the __iadd__ method:
class Cart:
    def __init__(self):
        self.items = []

    @property
    def total(self):
        return sum([item.amount for item in self.items])

    def __str__(self):
        if not self.items:
            return "The cart is empty"

        return "\n".join([str(item) for item in self.items])

    def __iadd__(self, item):
        if not isinstance(item, Item):
            raise ValueError("The item must be an instance of Item")

        self.items.append(item)
        return self


# In the __iadd__ method, we raise a ValueError if the item is not an instance of the Item class. Otherwise, we add the item to the items list attribute.
# The total property returns the sum of all items.
# The __str__ method returns the string 'The cart is empty' if the cart has no item. Otherwise, it returns a string that contains all items separated by a newline.


# Third, use the += operator to add an item to the cart:
if __name__ == "__main__":
    cart = Cart()

    cart += Item("Apple", 5, 2)
    cart += Item("Banana", 20, 1)
    cart += Item("Orange", 10, 1.5)

    print(cart)
    # print the total line
    print("-" * 30)
    print("Total: $", cart.total)

"""
Apple   5       $2      $10
Banana  20      $1      $20
Orange  10      $1.5    $15.0
------------------------------
Total: $ 45.0
"""


# Summary
# Operator overloading allows a class to use built-in operators.
