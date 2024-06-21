from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import datetime
from time import sleep
from typing import List

# The Memento class is the base class for all mementos
class Memento(ABC):
    @property
    @abstractmethod
    def date(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

# The GameState class is a dataclass representing the state of the game
@dataclass
class GameState:
    level: int
    score: int
    inventory: List[str] = field(default_factory=list)

    def __str__(self):
        return f"Level: {self.level}, Score: {self.score}, Inventory: {self.inventory}"

# The Game class is the Originator
class Game:
    def __init__(self):
        self.state = GameState(1, 0, [])

    def play(self):
        self.state.level += 1
        self.state.score += 100
        self.state.inventory.append(f"Item{len(self.state.inventory) + 1}")

    def save(self) -> Memento:
        return self._GameStateMemento(datetime.datetime.now(), self.state)

    def restore(self, memento: Memento):
        self.state = memento.state
    
    # The GameStateMemento class is the concrete memento class
    # This class is encapsulated within the Game class
    class _GameStateMemento(Memento):
        def __init__(self, date, state: GameState):
            self._date = date
            self._state = GameState(state.level, state.score, state.inventory.copy())

        @property
        def date(self):
            return self._date

        @property
        def state(self):
            return self._state
        
        def __str__(self):
            return f"[Snapshot @ {self._date}] {self._state}"

# The GameStateCaretaker class is responsible for managing the game state's mementos
class GameStateCaretaker:
    def __init__(self, game: Game):
        self._game = game
        self._mementos: List[Memento] = []

    def backup(self):
        memento = self._game.save()
        print(f"Saving game state at {memento.date}")
        self._mementos.append(memento)

    def undo(self):
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
    sleep(.5) # Simulating a delay between game states
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
