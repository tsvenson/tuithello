"""
Tuithello is an Othello game that runs in the terminal.
"""
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Label

from tuithello.board import Board


class TuithelloApp(App):
    """The Tuithello app to run the game."""
    CSS_PATH = "tuithello.tcss"

    TITLE = "Tuithello"

    BINDINGS = [
        ("ctrl+d", "toggle_dark", "Toggle dark mode"),
        ("ctrl+q", "quit", "Quit the game")
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="board"):
            yield Board()
        yield Footer()
    
    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

    def action_quit(self) -> None:
        self.app.exit()


def app():
    game = TuithelloApp()
    game.run()


if __name__ == "__main__":
    app()
