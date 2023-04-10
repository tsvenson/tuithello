from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Button


class Square(Button):
    """Individual board squares."""

    @staticmethod
    def square_id_gen(row: int, col: int) -> str:
        """Generates row/column ID for each square on the board.
        
        Args:
            row (int): The row of the square.
            col (int): The column of the square.
        
        Returns:
            str: An ID string for the square.
        """
        return f"square-{row}-{col}"
    
    def __init__(self, row: int, col: int) -> None:
        """Initialize the square.

        Args:
            row (int): The row of the square.
            col (int): The column of the square.
        """
        super().__init__("", id=self.square_id_gen(row, col))
        self.row: int = row
        self.col: int = col


class Board(Widget):
    """Creates and initializes the board and squares."""

    def compose(self) -> ComposeResult:
        """Compose the square grid.
        
        Returns:
            ComposeResults: The squares on the board grid.
        """
        for row in range(1, 9):
            for col in range(1, 9):
                yield Square(row, col)
