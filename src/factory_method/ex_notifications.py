"""
Factory Method Pattern Example: Notifications System

In this example, we use the Factory Method pattern to
create different types of notifications.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
import re

class Notification(ABC):
    """
    Abstract notification class.
    """

    @abstractmethod
    def send(self, message: str, recipient: str):
        pass

    @abstractmethod
    def verify_recipient(self, recipient: str) -> bool:
        pass

    def sanitize_recipient(self, recipient: str) -> str:
        """
        Sanitize recipient by stripping leading and trailing whitespaces.
        """
        return recipient.strip()


class EmailNotification(Notification):
    """
    Email notification class.
    """

    def send(self, message: str, recipient: str):
        print(f"Sending Email to {recipient}: {message}")

    def sanitize_recipient(self, recipient: str) -> str:
        bad_chars = r'[^a-zA-Z0-9@.]'
        return re.sub(bad_chars, '', super().sanitize_recipient(recipient))

    def verify_recipient(self, recipient: str) -> bool:
        return bool(re.search(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+', recipient))


class SMSNotification(Notification):
    """
    SMS notification class.
    """

    def send(self, message: str, recipient: str):
        print(f"Sending SMS to {recipient}: {message}")

    def sanitize_recipient(self, recipient: str) -> str:
        sanitized = super().sanitize_recipient(recipient)
        pattern = r'[^0-9+]'
        return re.sub(pattern, '', sanitized)

    def verify_recipient(self, recipient: str) -> bool:
        if recipient.startswith("+"):
            recipient = recipient[1:]

        if not recipient.isnumeric():
            print(f"Recipient contains non-numeric characters: {recipient}")
            return False
        return True


class PushNotification(Notification):
    """
    Push notification class.
    """

    pattern = r'[^a-z0-9_]'

    def send(self, message: str, recipient: str):
        print(f"Sending Push notification to {recipient}: {message}")

    def sanitize_recipient(self, recipient: str) -> str:
        sanitized = super().sanitize_recipient(recipient).lower()
        return re.sub(PushNotification.pattern, '', sanitized)

    def verify_recipient(self, recipient: str) -> bool:
        return not bool(re.search(PushNotification.pattern, recipient))


class NotificationFactory(ABC):
    """
    Notification factory base class.
    """

    @abstractmethod
    def create_notification(self) -> Notification:
        pass


class EmailNotificationFactory(NotificationFactory):
    """
    Factory for Email notifications.
    """

    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSNotificationFactory(NotificationFactory):
    """
    Factory for SMS notifications.
    """

    def create_notification(self) -> Notification:
        return SMSNotification()


class PushNotificationFactory(NotificationFactory):
    """
    Factory for Push notifications.
    """

    def create_notification(self) -> Notification:
        return PushNotification()


def send_notification(factory: NotificationFactory, message: str, recipient: str):
    """
    Sends a notification using the specified factory.

    Args:
        factory (NotificationFactory): The factory to create the notification.
        message (str): The message to send.
        recipient (str): The recipient's identifier.
    """
    notification = factory.create_notification()
    if not notification.verify_recipient(recipient):
        recipient = notification.sanitize_recipient(recipient)
        print(f"Did you mean {recipient} as a recipient?")
    else:
        notification.send(message, recipient)


if __name__ == "__main__":
    """
    Example usage of sending notifications via different methods.
    """
    send_notification(EmailNotificationFactory(), "Hello, Email user!", "in^valid@user.$com")
    send_notification(EmailNotificationFactory(), "Hello, Email user!", "user@example.com")
    print()
    send_notification(SMSNotificationFactory(), "Hello, SMS user!", "+#123-456-7890")
    send_notification(SMSNotificationFactory(), "Hello, SMS user!", "+1234567890")
    print()
    send_notification(PushNotificationFactory(), "Hello, Push user!", "Some_user-123$")
    send_notification(PushNotificationFactory(), "Hello, Push user!", "push_user")
