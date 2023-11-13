from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import chess


class ChessButton(Button):
    def __init__(self, row, col, **kwargs):
        super(ChessButton, self).__init__(**kwargs)
        self.row = row
        self.col = col


class ChessGrid(GridLayout):
    def __init__(self, **kwargs):
        super(ChessGrid, self).__init__(**kwargs)
        self.cols = 8
        self.rows = 8
        self.board = chess.Board()

        for row in range(8):
            for col in range(8):
                piece = self.board.piece_at(chess.square(col, 7 - row))
                button = ChessButton(
                    row=row, col=col, text=str(piece) if piece else '')
                button.bind(on_release=self.on_button_click)
                self.add_widget(button)

    def on_button_click(self, instance):
        row, col = instance.row, instance.col
        square = chess.square(col, 7 - row)
        legal_moves = [move.uci() for move in self.board.legal_moves]

        if square in legal_moves:
            self.board.push(chess.Move.from_uci(square))

        for child in self.children:
            if isinstance(child, ChessButton):
                piece = self.board.piece_at(
                    chess.square(child.col, 7 - child.row))
                child.text = str(piece) if piece else ''


class ChessApp(App):
    def build(self):
        return ChessGrid()


if __name__ == '__main__':
    ChessApp().run()
