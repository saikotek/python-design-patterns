"""
Facade Design Pattern

Example: Third-Party Email Library
"""

class EmailLib:
    """
    Some complex, third-party library for sending emails.
    """

    def __init__(self):
        """Initializes the EmailLib class."""
        pass

    def set_sender(self, sender_email: str) -> None:
        self.sender = sender_email

    def set_receiver(self, receiver_email: str) -> None:
        self.receiver = receiver_email

    def set_subject(self, subject: str) -> None:
        self.subject = subject

    def set_body(self, body: str) -> None:
        self.body = body

    def send_email(self) -> str:
        return f"Email sent from {self.sender} to {self.receiver} " \
            f"with subject '{self.subject}' and body '{self.body}'."


class EmailFacade:
    """
    Facade for simplifying the usage of the EmailLib.
    """

    def __init__(self):
        """Initializes the EmailFacade class."""
        self.email_lib = EmailLib()

    def send_email(self, sender: str, receiver: str, subject: str, body: str) -> str:
        """
        Simplifies the process of sending an email.

        Args:
            sender (str): The sender's email address.
            receiver (str): The receiver's email address.
            subject (str): The subject of the email.
            body (str): The body of the email.

        Returns:
            str: A confirmation message indicating the email was sent.
        """
        self.email_lib.set_sender(sender)
        self.email_lib.set_receiver(receiver)
        self.email_lib.set_subject(subject)
        self.email_lib.set_body(body)
        return self.email_lib.send_email()


if __name__ == "__main__":
    """
    Example usage of the EmailFacade to send an email.
    """
    facade = EmailFacade()
    result = facade.send_email(
        sender="sender@example.com",
        receiver="receiver@example.com",
        subject="Test Email",
        body="This is a test email."
    )
    print(result)
