import gamemodel

#structure in weights:
#gamestate, move, weight

class AI:

    # game = gamemodel.game()
    # field = ""
    # for row in game.field:
    #     for i in row:
    #         add = '2' if i == -1 else str(i)
    #         field += add
    # weights = [[field, 11, 0.9]]

    def read_weights(self):
        try:
            weightfile = open("weights.txt", "r")
        except FileNotFoundError:
            weightfile = open("weights.txt", "w")

        if weightfile.mode == 'r':
            self.weights = []
            fl = weightfile.readlines()
            for line in fl:
                print("Line: ", line)
                words = []
                for word in line.split():
                    print("Word: ", word)
                    words.append(word)
                self.weights.append(words)

    def save_weights(self):
        weightfile = open("weights.txt", "w")
        for w in self.weights:
            print("writing...")
            info = str(w[0]) +" "+ str(w[1]) +" "+ str(w[2])
            weightfile.write(info)

def get_valid_moves(game):
    valid_moves = []
    for row in range(0,3):
        for column in range(0,3):
            if gamemodel.move_is_valid((row,column), game):
                valid_moves.append((row,column))


def get_best_move(current_field):
    pass


def evaluateWin(made_moves):
    pass


def evaluateLoose(made_moves):
    pass


def evaluateGame(madeMoves, winner):
    for i in (0,1):
        if madeMoves[i] != []:
            if winner == i:
                evaluateWin(madeMoves[i])
            else:
                evaluateLoose(madeMoves[i])