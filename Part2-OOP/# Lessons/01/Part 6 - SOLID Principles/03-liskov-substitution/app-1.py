"""
Liskov Substitution Principle
- The Liskov substitution principle states that a child class must be substitutable for its parent class.

- Liskov substitution principle aims to ensure that the child class can assume the place of its parent class without causing any errors.


"""

# Consider the following example:
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message, email):
        pass


class Email(Notification):
    def notify(self, message, email):
        print(f"Send {message} to {email}")


class SMS(Notification):
    def notify(self, message, phone):
        print(f"Send {message} to {phone}")


if __name__ == "__main__":
    notification = SMS()
    notification.notify("Hello", "john@test.com")


# In this example, we have three classes: Notification, Email, and SMS. The Email and SMS classes inherit from the Notification class.
# The Notification abstract class has notify() method that sends a message to an email address.
# The notify() method of the Email class sends a message to an email, which is fine.
# However, the SMS class uses a phone number, not an email, for sending a message. Therefore, we need to change the signature of the notify() method of the SMS class to accept a phone number instead of an email.
