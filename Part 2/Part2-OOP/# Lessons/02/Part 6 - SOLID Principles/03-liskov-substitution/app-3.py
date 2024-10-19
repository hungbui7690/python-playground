"""
Conform with the Liskov substitution principle
- The Liskov substitution principle states that a child class must be substitutable for its parent class.

"""

from abc import ABC, abstractmethod


# First, redefine the notify() method of the Notification class so that it doesn’t include the email parameter:
class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass


# Second, add the email parameter to the __init__ method of the Email class:
class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')


# Third, add the phone parameter to the __init__ method of the SMS class:
class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


# Fourth, change the NotificationManager class:
class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)


if __name__ == "__main__":
    contact = Contact("John Doe", "john@test.com", "(408)-888-9999")

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send("Hello John")  # Send "Hello John" to (408)-888-9999

    notification_manager.notification = email_notification
    notification_manager.send("Hi John")  # Send "Hi John" to john@test.com
