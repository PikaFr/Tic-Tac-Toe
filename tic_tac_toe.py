import os, time

class morpion :
    # Variables
    board = ["-","-","-","-","-","-","-","-","-"]
    win_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    in_arow = [1, 1, 1]
    cache = 0
    default_player = 0
    win = 0
    who_win = 0

    def symbol(self, player_id):
        if player_id == 0:
            return "X"
        return "O"



    def __init__(self):
        point = [".", "..", "...", ".", "..", "..."]
        for i in range(0, 6):
            os.system('cls')
            print("Starting the program", point[i])
            time.sleep(0.6)
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



    #Automatily restart a new round if the gmae is not finished
    def round(self):
        while int(self.win) == 0:
            self.play()
            self.state_win()
            self.state_egality()
            self.display()
        if int(self.win) == 1:
            print("The player",self.who_win,"win the game")
            return
        if int(self.win) == 2:
            print("Egality")
            return



    # Ask and place a mark in the board
    def play(self):
        symbol = self.symbol(self.default_player)
        position_brut = input("It's up player " + symbol +" to play where do you want to play (1 to 9) : ")
        try:
            position = int(position_brut) - 1
            if position >= 0 and position <= 8:
                if self.board[position] != "-":
                    print("You cannot place your mark into a busy case")
                    return
                self.board[position] = symbol
                print("--------")
                if self.default_player != 1:
                    self.default_player = 1
                    return
                else:
                    self.default_player = 0
                    return
            print("Please, enter a number between 1 and 9\n--------")
            return
        except:
            print("This is not a number\n--------")
            return



    # Display the board
    def display(self):
        for n in [6, 3, 0]:
            print(self.board[0+n],self.board[1+n],self.board[2+n])
        print("--------")



    #Verify if state of the game is egalilty
    def state_egality(self):
        if self.win != 1:
            self.win = 2
            for i in range(0, 9):
                if self.board[i] == "-":
                    self.win = 0




    #Verify if state of the game is win
    def state_win(self):
        self.win = 3
        for d in ["X", "O"]:
            self.state_win_xo(d)


    def state_win_xo(self, xo):
        for h in range(0, 7):
            self.state_win_possibility(h, xo)


    def state_win_possibility(self, index, xo):
        cache_board = [0, 0, 0]
        for j in [0, 1, 2]:
            if self.board[self.win_board[index][j]] == xo:
                cache_board[j] = 1
            if cache_board == self.in_arow:
                self.who_win = xo
                self.win = 1
                return



game = morpion()
game.round()