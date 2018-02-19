import gamemodel, math, random
from decimal import Decimal

class Parent_AI:

    def __init__(self, game):
        self.weights = []
        self.read_weights()
        self.game = game

    def sigmoid(self, x):
        x = Decimal(x)
        return Decimal(1 / (1 + x.exp()))

    def rev_sigmoid(self,y):
        y = Decimal(y)
        if (y == 0):
            print(y)
        inner = (1/y)-1
        return Decimal(- Decimal(inner).ln())

    def read_weights(self):
        try:
            weightfile = open("weights.txt", "r")
        except FileNotFoundError:
            weightfile = open("weights.txt", "w")

        if weightfile.mode == 'r':
            self.weights = []
            fl = weightfile.readlines()
            for line in fl:
                words = []
                for word in line.split():
                    words.append(word)
                self.weights.append(words)

    def save_weights(self):
        new = False
        weightfile = open("weights.txt", "w")
        for w in self.weights:
            info = str(w[0]) +" "+ str(w[1]) +" "+ str(w[2])+" "+ str(w[3]) +"\n"
            if Decimal(w[3]) >= 2**20:
                new = True
                break
            weightfile.write(info)
        if new:
            print("new")
            for w in self.weights:
                w[3] = Decimal(w[3])/2
                info = str(w[0]) +" "+ str(w[1]) +" "+ str(w[2])+" "+ str(w[3]) +"\n"
                weightfile.write(info)

    def evaluateGame(self, madeMoves, winner):
        for i in (0,1):
            if madeMoves[i] != []:
                if winner == i:
                    self.evaluate(madeMoves[i], 'w', i)
                elif winner == 1-i:
                    self.evaluate(madeMoves[i], 'l', i)
                else:
                    self.evaluate(madeMoves[i], 't', i)

    def get_valid_moves(self, game):
        valid_moves = []
        for row in range(0, 3):
            for column in range(0, 3):
                if gamemodel.move_is_valid((row, column), game):
                    valid_moves.append((row, column))
        return valid_moves

    def randomMove (self, field):
        valid_moves = self.get_valid_moves(self.game)
        best_move = valid_moves[random.randrange(0, len(valid_moves))]

        return best_move