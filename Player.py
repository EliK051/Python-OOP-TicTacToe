from Board import Board
import random

class Player:
    def __init__(self,is_turn,type,board):
        self.name=""
        self.symbol=''
        self.position=None
        self.is_turn=is_turn
        self.type=type
        self.board=board


    def set_name(self,name=""):
        if self.type=='computer':
            self.name=name
        elif self.type=='human':
            print('Enter your name:')
            self.name = input()
            print('Hello, ' + self.name)


    def set_symbol(self,symbol=False):
        if self.type == 'computer':
            self.symbol = symbol
        elif self.type == 'human':
            print('Enter your symbol:')
            x=input()
            if x=='X' or x=='O':
                self.symbol=x
                print('your chosen symbol is : ' + self.symbol)
            else:
                print("invalid input, choose either capital O or capital X")



    def toggle_turn(self):
        if self.is_turn==False:
            self.is_turn=True
        else:
            self.is_turn=False


    def set_position(self):

        if self.type=='computer':

            chosen = random.choice(self.board.list)
            self.is_position_valid(chosen)

        else:
            while (not self.is_position_valid()):
                continue
        self.board.board[self.position[0]][self.position[1]]=self.symbol


    def is_position_valid(self,x=False):
        try:
            if(self.type=='human'):
                x = int(input('Enter position:'))
                if x < 1 or x > 10:
                    print("invalid input, choose a position between 1 and 9")
                    return False
        except:
            print("invalid input, choose a position between 1 and 9")
            return False
        else:
            position = self.board.position_converter(x)
            if self.board.board[position[0]][position[1]] == '-':
                self.position = position
                print(x)
                self.board.list.remove(x)
                return True
            else:
                print(f'space taken by {self.board.board[position[0]][position[1]]}')
                return False
        # except:
        #     print("invalid input, choose a position between 1 and 9")
        #     return False





        # exp=Player(5,True,'Human')
#
# exp.what()
# exp.type='human'
# exp.set_name()
# exp.set_symbol()
# print(exp.symbol)
