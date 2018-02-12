import random
import gamemodel

#structure in weights:
#gamestate, move, playernr, weight

class AI:

    def __init__(self, game):
        self.weights = []
        self.read_weights()
        self.game = game

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
        weightfile = open("weights.txt", "w")
        for w in self.weights:
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
                    pass

    def evaluate(self, made_moves, result, player):
        #move: (game.field, (row,column))
        movecount = len(made_moves)
        for move in range(0, movecount):
            fieldstr = made_moves[move][0]
            movestr = str(made_moves[move][1][0])+str(made_moves[move][1][1])
            playerstr = str(player)

            found = False
            for field in self.weights:
                if field[0] == fieldstr and field[1] == movestr and field[2] == playerstr:
                    amount = ((move+1)/movecount)**2
                    w = float(field[3])+amount if result == 'w' else float(field[3])-amount
                    field[3] = w
                    found = True
            if(not found):
                amount = ((move+1)/movecount)**2
                w = amount if result == 'w' else (-amount)
                self.weights.append([fieldstr,movestr,player,w])

    def get_best_move(self, current_field):
        valid_moves = self.get_valid_moves(self.game)
        if len(valid_moves) == 1:#dont search if only one move left
            return valid_moves[0]
        relevantNodes = []
        for node in self.weights:
            if node[0] == current_field:
                relevantNodes.append(node)

        best_move = valid_moves[random.randrange(len(valid_moves))]
        best_move_value = -2
        for move in valid_moves:
            move_str = str(move[0])+str(move[1])
            for node in relevantNodes:
                if move_str == node[1]:
                    if float(node[3]) > best_move_value:
                        best_move = move
                        best_move_value = float(node[3])
        return best_move

    def get_valid_moves(self, game):
        valid_moves = []
        for row in range(0, 3):
            for column in range(0, 3):
                if gamemodel.move_is_valid((row, column), game):
                    valid_moves.append((row, column))
        return valid_moves