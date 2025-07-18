class Board:
    def __init__(self):
        self.board = [' ',' ',' ',
                      ' ',' ',' ',
                      ' ',' ',' ']

    def print_board(self):
        print('\n')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])   
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def update_board(self,position,type):
        try:
            if self.board[position - 1] == ' ':
                self.board[position - 1] = type
                return True

            else:
                print('Position already selected. select another position: ')  
                return False  

        except:
            print('Invalid position! select another position.')

    def check_winner(self,type):
        if (self.board[0] == type and self.board[1] == type and self.board[2]==type) or \
           (self.board[3] == type and self.board[4] == type and self.board[5] == type) or \
           (self.board[6] == type and self.board[7] == type and self.board[8] == type) or \
           (self.board[0] == type and self.board[3] == type and self.board[6] == type) or \
           (self.board[1] == type and self.board[4] == type and self.board[7] == type) or \
           (self.board[2] == type and self.board[5] == type and seelf.board[8] == type) or \
           (self.board[0] == type and self.board[4] == type and self.board[8] == type) or \
           (self.board[2] == type and self.board[4] == type and self.board[6] == type):

           return True
        else:
            return False

    def check_draw(self):
        if ' ' not in self.board:
            return True
        else:
            return False            

class Player:
    def __init__(self,type):
        self.type = type
        self.name = self.get_name()    

    def get_name(self):
        if self.type == 'x':
            name = input('Player selecting x, enter your name: ')

        else:
            name = input('Player selecting o, enter your name: ')    

        return name    

class Game:
    def __init__(self):      
        self.board = Board()
        self.player1 = Player('x')
        self.player2 = Player('o')
        self.current_player = self.player1

    def play(self):
        while True:
            try:
                message = f'{self.current_player.name},enter the position(1,9):'
                position = int(input(message))

                if self.board.update_board(position,self.current_player.type):
                    self.board.print_board()

                    if self.board.check_winner(self.current_player.type):
                        print(self.current_player.name,'wins!')
                        break

                    elif self.board.check_draw():
                        print('Game is a draw!')
                        break

                    else:        

                        if self.current_player == self.player1:
                            self.current_player = self.player2

                        else:
                            self.current_player = self.player1

            except:
                print('Invalid input! Enter a number between 1 and 9.')
                
game = Game()
game.play()