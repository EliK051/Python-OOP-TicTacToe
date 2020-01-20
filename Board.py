class Board:

    def __init__(self):
        self.board=[]
        self.is_board_full=False
        self.init_count=0
        self.list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def init_board(self):
        if self.init_count==0:
            self.board=[[1,2,3],
                        [4,5,6],
                        [7,8,9]]
            self.init_count+=1
        else:
            self.board = [['-','-','-'],
                          ['-', '-','-'],
                          ['-', '-', '-']]


    def display_board(self):
        for i in range(0,3):
            emp=""
            emp += "|"
            for j in range(0,3):

                emp+=str(self.board[i][j])
                emp += "|"
            print(emp)
        print('------------')
    def position_converter(self,position):
        if position<=3:
            return [0,position-1]
        elif position<=6:
            return [1, position - 4]
        else:
            return [2, position - 7]




    def set_board(self,position,symbol):
        position=self.position_converter(position)
        self.board[position[0]][position[1]]=symbol

    def check_rows(self):
        for i in range(0,3):
            o = 0
            x = 0
            for j in range(0,3):
                if self.board[i][j]=='X':
                    x+=1
                elif self.board[i][j]=='O':
                    o+=1
            if x == 3 or o == 3:
                return self.board[i][j]
        return False

    def check_columns(self):
        for j in range(0,3):
            o = 0
            x = 0
            for i in range(0,3):
                if self.board[i][j]=='X':
                    x+=1
                elif self.board[i][j]=='O':
                    o+=1
            if x == 3 or o == 3:
                return self.board[i][j]
        return False

    def check_diagonals(self):
        o = 0
        x = 0
        for j in range(0,3):
            if self.board[j][j] == 'X':
                x += 1
            elif self.board[j][j] == 'O':
                o += 1
        if x == 3 or o == 3:
            return self.board[j][j]
        o = 0
        x = 0

        if self.board[0][2] == self.board[1][1] == self.board[2][0] =='X' or \
            self.board[0][2] == self.board[1][1] == self.board[2][0] =='O':
            return self.board[1][1]
        return False

    def check_sequence(self):
        if self.check_rows():
            return self.check_rows()
        elif self.check_columns():
            return self.check_rows()
        else:
            return self.check_diagonals()

    def check_full_board(self):
        full=0
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j]=='X' or self.board[i][j]=='O':
                    full+=1
        if full==9:
            self.is_board_full=True

        else :
            self.is_board_full=False



