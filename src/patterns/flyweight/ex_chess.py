"""
Flyweight Pattern

Example: Chess Pieces factory reusing shared pieces
"""
from typing import Dict, Tuple


class ChessPiece:
    """Chess piece class representing intrinsic state (shared)."""

    def __init__(self, type: str, color: str) -> None:
        """
        Initializes a ChessPiece with a type and color.

        Args:
            type (str): The type of the chess piece (e.g., "rook").
            color (str): The color of the chess piece (e.g., "black").
        """
        self.type = type  # Intrinsic state
        self.color = color  # Intrinsic state

    def __repr__(self) -> str:
        return f"{self.color} {self.type}"

class ChessPieceFactory:
    """Factory to manage chess pieces and ensure reuse."""

    def __init__(self) -> None:
        """Initializes the ChessPieceFactory with an empty pieces dictionary."""
        self.pieces: Dict[Tuple[str, str], ChessPiece] = {}

    def get_piece(self, type: str, color: str) -> ChessPiece:
        """
        Returns a ChessPiece with the given type and color, creating it if necessary.

        Args:
            type (str): The type of the chess piece (e.g., "rook").
            color (str): The color of the chess piece (e.g., "black").

        Returns:
            ChessPiece: The requested ChessPiece.
        """
        key = (type, color)
        if key not in self.pieces:
            self.pieces[key] = ChessPiece(type, color)
        return self.pieces[key]

class ChessPieceContext:
    """Context class representing extrinsic state (unique)."""

    def __init__(self, piece: ChessPiece, position: Tuple[int, int]) -> None:
        """
        Initializes a ChessPieceContext with a piece and a position.

        Args:
            piece (ChessPiece): The flyweight chess piece object.
            position (Tuple[int, int]): The position of the chess piece on the board.
        """
        self.piece = piece  # Flyweight object
        self.position = position  # Extrinsic state

    def __repr__(self) -> str:
        return f"{self.piece} at {self.position}"


if __name__ == "__main__":
    # Client code
    factory = ChessPieceFactory()

    # Creating chess pieces on the board
    positions = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 0), (1, 0)]
    types = ["rook", "knight", "bishop", "queen", "rook", "knight"]
    colors = ["black", "black", "white", "white", "black", "black"]

    contexts = [ChessPieceContext(factory.get_piece(type, color), pos)
                for pos, type, color in zip(positions, types, colors)]

    # Displaying the chess pieces and their positions
    for context in contexts:
        print(context)

    # Demonstrating that the same instances are reused
    print("\nDemonstrating reuse of existing pieces:")
    print(f"Context 1 piece id: {id(contexts[0].piece)}")
    print(f"Context 5 piece id: {id(contexts[4].piece)}")
    print(f"Context 2 piece id: {id(contexts[1].piece)}")
    print(f"Context 6 piece id: {id(contexts[5].piece)}")

    assert contexts[0].piece is contexts[4].piece  # Rook (black) is reused
    assert contexts[1].piece is contexts[5].piece  # Knight (black) is reused
