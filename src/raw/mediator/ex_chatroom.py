# Mediator Design Pattern real-world example
# This example demonstrates the Mediator design pattern that relies on the Observer pattern 
# to notify all users in a chatroom when a user sends a message.

class ChatRoom:
    def __init__(self):
        self.users = []

    def subscribe(self, user):
        self.users.append(user)

    def unsubscribe(self, user):
        self.users.remove(user)

    def notify(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message)

class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom
        self.chatroom.subscribe(self)

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.chatroom.notify(message, self)

    def receive(self, message):
        print(f"{self.name} receives: {message}")

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
