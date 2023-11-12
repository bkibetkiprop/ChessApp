# Import Kivy modules
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

# Import chess module for basic chess logic
import chess
import chess.svg


class ChessBoard(GridLayout):
    def __init__(self, **kwargs):
        super(ChessBoard, self).__init__(**kwargs)
        self.cols = 8
        self.rows = 8
        self.board = chess.Board()
        self.buttons = [[None for _ in range(8)] for _ in range(8)]

        for row in range(8):
            for col in range(8):
                btn = Button(
                    text=str(self.board.piece_at(chess.square(col, 7 - row))),
                    on_press=self.on_button_press,
                    size_hint=(None, None),
                )
                self.buttons[row][col] = btn
                self.add_widget(btn)

    def update_board(self):
        for row in range(8):
            for col in range(8):
                self.buttons[row][col].text = str(
                    self.board.piece_at(chess.square(col, 7 - row)))

    def on_button_press(self, instance):
        for row in range(8):
            for col in range(8):
                if instance == self.buttons[row][col]:
                    move = chess.Move.from_uci(
                        f"{chr(ord('a') + col)}{row + 1}")
                    if move in self.board.legal_moves:
                        self.board.push(move)
                        self.update_board()


class ChessApp(App):
    def build(self):
        return ChessBoard()


if __name__ == '__main__':
    ChessApp().run()
