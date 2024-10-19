"""
Liskov Substitution Principle
- The Liskov substitution principle states that a child class must be substitutable for its parent class.

- Liskov substitution principle aims to ensure that the child class can assume the place of its parent class without causing any errors.


"""

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


# The following NotificationManager class uses the Notification object to send a message to a Contact:
class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class NotificationManager:
    def __init__(self, notification, contact):
        self.contact = contact
        self.notification = notification

    def send(self, message):
        if isinstance(self.notification, Email):
            self.notification.notify(message, contact.email)
        elif isinstance(self.notification, SMS):
            self.notification.notify(message, contact.phone)
        else:
            raise Exception("The notification is not supported")


if __name__ == "__main__":
    contact = Contact("John Doe", "john@test.com", "(408)-888-9999")
    notification_manager = NotificationManager(SMS(), contact)
    notification_manager.send("Hello John")


# The send() method of the NotificationManager class accepts a notification object. It checks whether the notification is an instance of the Email or SMS and passes the email and phone of contact to the notify() method respectively.
