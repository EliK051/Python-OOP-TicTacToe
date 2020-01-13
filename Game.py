from Player import Player
from Board import Board


class Game:
    def __init__(self):
        self.is_game_still_on = True
        self.board = Board()
        self.player1=Player(True,'human',self.board)
        self.player2=Player(False,'computer',self.board)
        self.winner_symbol=None


    def init_players(self):
        self.player1.set_name()
        self.player2.set_name('RoboCop')
        self.player1.set_symbol()
        if self.player1.symbol=='X':
            self.player2.set_symbol('O')
        else:
            self.player2.set_symbol('X')


    def check_winner(self):
        is_win=self.board.check_sequence()
        if is_win:
            self.winner_symbol=is_win
            self.is_game_still_on=False
            if is_win==self.player1.symbol:
                print(f"The winner is : {self.player1.type}")
            else:
                print(f"The winner is : {self.player2.type}")
            self.board.display_board()
    def check_tie(self):
        self.board.check_full_board()
        if self.board.is_board_full:
            print(f'it is a tie')
            self.is_game_still_on=False
            self.board.display_board()

    def play_game(self):

        while(not self.player1.symbol):
            self.init_players()
        self.board.init_board()
        self.board.display_board()
        self.board.init_board()
        while(self.is_game_still_on):
            self.board.display_board()
            if self.player1.is_turn:

                self.player1.set_position()
                self.player1.toggle_turn()
                self.player2.toggle_turn()
            elif self.player2.is_turn:

                self.player2.set_position()
                self.player1.toggle_turn()
                self.player2.toggle_turn()
            self.check_winner()
            self.check_tie()

