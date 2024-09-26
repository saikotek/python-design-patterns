"""
Mediator Pattern Example: Chat Room

This example demonstrates the Mediator design pattern that relies on the Observer pattern
to notify all users in a chatroom when a user sends a message.
"""
from __future__ import annotations


class ChatRoom:
    """ChatRoom acts as a mediator for communication between users."""

    def __init__(self) -> None:
        self.users = []

    def subscribe(self, user: User) -> None:
        """
        Subscribes a user to the chat room.
        """
        self.users.append(user)

    def unsubscribe(self, user: User) -> None:
        """
        Unsubscribes a user from the chat room.
        """
        self.users.remove(user)

    def notify(self, message: str, sender: User) -> None:
        """
        Notifies all users in the chat room except the sender.
        """
        for user in self.users:
            if user != sender:
                user.receive(message)

class User:
    """User represents a user in the chat room."""

    def __init__(self, name: str, chatroom: ChatRoom) -> None:
        """
        Initializes the user with a name and subscribes to a chat room.
        """
        self.name = name
        self.chatroom = chatroom
        self.chatroom.subscribe(self)

    def send(self, message: str) -> None:
        """
        Sends a message to the chat room.
        """
        print(f"{self.name} sends: {message}")
        self.chatroom.notify(message, self)

    def receive(self, message: str) -> None:
        """
        Receives a message from the chat room.
        """
        print(f"{self.name} receives: {message}")


if __name__ == "__main__":
    # Example usage
    chatroom = ChatRoom()

    user1 = User("Alice", chatroom)
    user2 = User("Bob", chatroom)
    user3 = User("Charlie", chatroom)

    user1.send("Hello, everyone!")
    user2.send("Hi, Alice!")
    user3.send("Hey folks!")

    chatroom.unsubscribe(user2)
    user1.send("Bob left the chat")
