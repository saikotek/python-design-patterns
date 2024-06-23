"""
Memento Design Pattern

Example: Saving and restoring the state of a game
"""
from dataclasses import dataclass, field
import datetime
from time import sleep
from typing import List, Protocol


class Memento(Protocol):
    """The Memento protocol defines the interface for mementos."""

    @property
    def date(self):
        """Gets the date when the memento was created."""
        ...

    def __str__(self):
        """Returns a string representation of the memento."""
        ...

@dataclass
class GameState:
    """The GameState class is a dataclass representing the state of the game."""
    level: int
    score: int
    inventory: List[str] = field(default_factory=list)

    def __str__(self):
        """Returns a string representation of the game state."""
        return f"Level: {self.level}, Score: {self.score}, Inventory: {self.inventory}"

class Game:
    """The Game class is the Originator. We want to save its state using mementos."""

    def __init__(self):
        """Initializes the game with the initial state."""
        self.state = GameState(1, 0, [])

    def play(self):
        """Simulates playing the game by changing the game state."""
        self.state.level += 1
        self.state.score += 100
        self.state.inventory.append(f"Item{len(self.state.inventory) + 1}")

    def save(self) -> Memento:
        """Saves the current game state to a memento."""
        return self._GameStateMemento(self.state)

    def restore(self, memento: Memento):
        """Restores the game state from a memento."""
        self.state = memento.state

    @dataclass(frozen=True)
    class _GameStateMemento(Memento):
        """The GameStateMemento class is the concrete memento class, encapsulated within the Game class."""
        _state: GameState
        _date: datetime.datetime = field(default_factory=datetime.datetime.now)

        @property
        def date(self):
            """Gets the date when the memento was created."""
            return self._date

        @property
        def state(self):
            """Gets the game state stored in the memento."""
            return self._state

        @state.setter
        def state(self, state: GameState):
            """Sets the game state stored in the memento."""
            self._state = GameState(state.level, state.score, state.inventory.copy())

        def __str__(self):
            """Returns a string representation of the memento."""
            return f"[Snapshot @ {self._date}] {self._state}"

class GameStateCaretaker:
    """The GameStateCaretaker class is responsible for managing the game state's mementos."""

    def __init__(self, game: Game):
        """Initializes the caretaker with a game instance."""
        self._game = game
        self._mementos: List[Memento] = []

    def backup(self):
        """Creates a backup of the current game state."""
        memento = self._game.save()
        print(f"Saving game state at {memento.date}")
        self._mementos.append(memento)

    def undo(self):
        """Restores the last saved game state."""
        if not self._mementos:
            print("No mementos to restore.")
            return
        memento = self._mementos.pop()
        print("Restoring game state to:", str(memento))
        self._game.restore(memento)


if __name__ == "__main__":
    # Example usage
    game = Game()
    caretaker = GameStateCaretaker(game)

    print(game.state)
    caretaker.backup()
    sleep(.5)  # Simulating a delay between game states
    game.play()

    print(game.state)
    caretaker.backup()
    game.play()

    print(game.state)
    caretaker.undo()
    print(game.state)
    caretaker.undo()
    print(game.state)
    caretaker.undo()  # Attempting to undo beyond the initial state
