class Check:

    def __init__(self):
        self.board = {
            'T1': ' ', 'T2': ' ', 'T3': ' ',
            'M1': ' ', 'M2': ' ', 'M3': ' ',
            'D1': ' ', 'D2': ' ', 'D3': ' '
        }

    def game_over(self):
        if self.board['T1'] == 'X' and self.board['T2'] == 'X' and self.board['T3'] == 'X':
            return 1
        elif self.board['M1'] == 'X' and self.board['M2'] == 'X' and self.board['M3'] == 'X':
            return 1
        elif self.board['D1'] == 'X' and self.board['D2'] == 'X' and self.board['D3'] == 'X':
            return 1
        elif self.board['T1'] == 'X' and self.board['M2'] == 'X' and self.board['D3'] == 'X':
            return 1
        elif self.board['T1'] == 'X' and self.board['M1'] == 'X' and self.board['D1'] == 'X':
            return 1
        elif self.board['T2'] == 'X' and self.board['M2'] == 'X' and self.board['D2'] == 'X':
            return 1
        elif self.board['T3'] == 'X' and self.board['M3'] == 'X' and self.board['D3'] == 'X':
            return 1
        elif self.board['T3'] == 'X' and self.board['M2'] == 'X' and self.board['D1'] == 'X':
            return 1

        elif self.board['T1'] == 'O' and self.board['T2'] == 'O' and self.board['T3'] == 'O':
            return 2
        elif self.board['M1'] == 'O' and self.board['M2'] == 'O' and self.board['M3'] == 'O':
            return 2
        elif self.board['D1'] == 'O' and self.board['D2'] == 'O' and self.board['D3'] == 'O':
            return 2
        elif self.board['T1'] == 'O' and self.board['M2'] == 'O' and self.board['D3'] == 'O':
            return 2
        elif self.board['T1'] == 'O' and self.board['M1'] == 'O' and self.board['D1'] == 'O':
            return 2
        elif self.board['T2'] == 'O' and self.board['M2'] == 'O' and self.board['D2'] == 'O':
            return 2
        elif self.board['T3'] == 'O' and self.board['M3'] == 'O' and self.board['D3'] == 'O':
            return 2
        elif self.board['T3'] == 'O' and self.board['M2'] == 'O' and self.board['D1'] == 'O':
            return 2
        return 0

    def new(self, option, p):
        if p == 1:
            if option.upper() in self.board and self.board[option.upper()] == ' ':
                self.board[option.upper()] = 'X'
        else:
            if option.upper() in self.board and self.board[option.upper()] == ' ':
                self.board[option.upper()] = 'O'
