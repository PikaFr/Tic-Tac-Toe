import os, time, random

class morpion :
    # Variables
    board = []
    in_arow = []
    cache_board = []
    default_player = 0
    win = 0
    who_win = 0
    size = 3    # This is used to set the size of the board

    # Make the board and the verif_cache with the correct size
    def make_board(self, board, in_arow):
        for t in range(self.size):
            board.append([])
            in_arow.append(1)
            for i in range(self.size):
                board[t].append("-")

    def reset_cache(self):
        global cache_board
        cache_board = []
        for t in range(self.size):
            cache_board.append(0)
        return cache_board

    def symbol(self, player_id):
        if player_id == 0:
            return "X"
        return "O"

    def __init__(self):
        point = [".", "..", "...", ".", "..", "..."]
        for i in range(0, 4):
            os.system('cls')
            print("Starting the program", point[i])
            time.sleep(0.4)
        os.system('cls')

        print("""
  __  __                  _                 _               _____       _        _____ _              _
 |  \/  |                (_)               | |             |  __ \     (_)      / ____| |            (_)
 | \  / | ___  _ __ _ __  _  ___  _ __     | |__  _   _    | |  | | ___ _  __ _| (___ | |_ __ _  __ _ _  ___ _ __ ___  ___
 | |\/| |/ _ \| '__| '_ \| |/ _ \| '_ \    | '_ \| | | |   | |  | |/ _ \ |/ _` |\___ \| __/ _` |/ _` | |/ _ \ '__/ _ \/ __|
 | |  | | (_) | |  | |_) | | (_) | | | |   | |_) | |_| |   | |__| |  __/ | (_| |____) | || (_| | (_| | |  __/ | |  __/\__ \\
 |_|  |_|\___/|_|  | .__/|_|\___/|_| |_|   |_.__/ \__, |   |_____/ \___| |\__,_|_____/ \__\__,_|\__, |_|\___|_|  \___||___/
                   | |                             __/ |              _/ |                       __/ |
                   |_|                            |___/              |__/                       |___/
        """)

        self.make_board(self.board, self.in_arow)

    # Ask if 1 or 2 players will play
    def ask_mode(self):
        global mode
        try:
            mode_num = int(input("Would you like to play with 1 or 2 players : "))
            if mode_num == 1 or mode_num == 2:
                if mode_num == 1: mode = 1
                if mode_num == 2: mode = 2
                print("--------")
                return
            print("Please, enter 1 or 2\n--------")
            self.ask_mode()
        except:
            print("This is not a number\n--------")
            self.ask_mode()

    #Automatily restart a new round if the gmae is not finished
    def round(self):
        self.ask_mode()
        self.display()
        while int(self.win) == 0:
            self.play()
            if mode != 2:
                self.play_ai()
            self.state_win()
            self.state_egality()
            self.display()
        if int(self.win) == 1:
            print("The player",self.who_win,"win the game")
            return
        if int(self.win) == 2:
            print("Egality")
            return

    def which_line(self, position):
        global line
        line = "error"
        if position >= 0 and position < self.size*self.size:
            for i in reversed(range(self.size)):
                n = i+1
                if position < self.size*n:line = i
        return line

    # An AI place a mark in the board
    def play_ai(self):
        symbol = self.symbol(self.default_player)
        cache_board = []
        try:
            for i in range(self.size):
                for n in range(self.size):
                    if self.board[i][n] == "-":
                        cache_board.append(i*self.size+n)
            position = random.choice(cache_board)
            self.which_line(position)
            if line != "error":
                self.board[line][position-line*self.size] = symbol
                if self.default_player != 1:
                    self.default_player = 1
                    return
                else:
                    self.default_player = 0
                    return
            self.play_ai()
        except: return

    # Ask and place a mark in the board
    def play(self):
        symbol = self.symbol(self.default_player)
        position_brut = input("It's up player " + symbol +" to play where do you want to play (1 to "+str(self.size*self.size)+") : ")
        try:
            position = int(position_brut) - 1
            self.which_line(position)
            if line != "error":
                if self.board[line][position-line*self.size] != "-":
                    print("You cannot place your mark into a busy case")
                    self.play()
                    return
                self.board[line][position-line*self.size] = symbol
                print("--------")
                if self.default_player != 1:
                    self.default_player = 1
                    return
                else:
                    self.default_player = 0
                    return
            print("Please, enter a number between 1 and ", self.size*self.size,"\n--------")
            self.play()
            return
        except:
            print("This is not a number\n--------")
            self.play()
            return

    # Display the board
    def display(self):
        for n in reversed(range(self.size)):
            for t in range(self.size):
                print(self.board[n][t], end=" ")
            print("")
        print("--------")

    #Verify if state of the game is egalilty
    def state_egality(self):
        if self.win != 1:
            self.win = 2
            for n in range(self.size):
                for i in range(self.size):
                    if self.board[n][i] == "-":
                        self.win = 0

    # Verify if state of the game is win
    def state_win(self):
        self.win = 3
        for d in ["X", "O"]:
            self.honrizontal(d)
            self.vertical(d)
            self.diagonal(d)

    def honrizontal(self, xo):
        for n in range(self.size):
            self.reset_cache()
            for j in range(self.size):
                if self.board[n][j] == xo:
                    cache_board[j] = 1
                if cache_board == self.in_arow:
                    self.who_win = xo
                    self.win = 1
                    return

    def vertical(self, xo):
        for n in range(self.size):
            self.reset_cache()
            for j in range(self.size):
                if self.board[j][n] == xo:
                    cache_board[j] = 1
                if cache_board == self.in_arow:
                    self.who_win = xo
                    self.win = 1
                    return

    def diagonal(self, xo):
        self.reset_cache()
        cache_board_2 = cache_board.copy()
        for t in range(self.size):
            if self.board[self.size-1-t][t] == xo:
                cache_board[t] = 1
            if self.board[t][t] == xo:
                cache_board_2[t] = 1
            if cache_board == self.in_arow or cache_board_2 == self.in_arow:
                self.who_win = xo
                self.win = 1

game = morpion()
game.round()