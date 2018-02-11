import random
import gamemodel

#structure in weights:
#gamestate, move, weight

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
            info = str(w[0]) +" "+ str(w[1]) +" "+ str(w[2])+"\n"
            weightfile.write(info)


    def evaluateGame(self, madeMoves, winner):
        for i in (0,1):
            if madeMoves[i] != []:
                if winner == i:
                    self.evaluateWin(madeMoves[i])
                elif winner == 1-i:
                    self.evaluateLoose(madeMoves[i])
                else:
                    # evaluateTie ?
                    pass

    def evaluateWin(self, made_moves):
        #move: (game.field, (row,column))
        print("eval win")
        movecount = len(made_moves)
        for move in range(0, movecount):
            fieldstr = self.field_to_text(made_moves[move][0])
            movestr = str(made_moves[move][1][0])+str(made_moves[move][1][1])

            found = False
            for field in self.weights:
                if field[0] == fieldstr and field[1] == movestr:
                    w = float(field[2])+((move+1)/movecount)
                    field[2] = w
                    found = True
            if(not found):
                w = (move+1)/movecount
                self.weights.append([fieldstr,movestr,w])

    def evaluateLoose(self, made_moves):
        print("eval loose")

    def get_best_move(self, current_field):
        valid_moves = self.get_valid_moves(self.game)
        if len(valid_moves) == 1:#dont search if only one move left
            return valid_moves[0]
        current_field = self.field_to_text(current_field)
        relevantNodes = []
        for node in self.weights:
            if node[0] == current_field:
                relevantNodes.append(node)

        best_move = valid_moves[random.randrange(len(valid_moves))]
        best_move_value = -1
        for move in valid_moves:
            move_str = str(move[0])+str(move[1])
            for node in relevantNodes:
                if move_str == node[1]:
                    if int(node[2]) > best_move_value:
                        best_move = move
        return best_move

    def get_valid_moves(self, game):
        valid_moves = []
        for row in range(0, 3):
            for column in range(0, 3):
                if gamemodel.move_is_valid((row, column), game):
                    valid_moves.append((row, column))
        return valid_moves

    def field_to_text(self, field):
         text = ""
         for row in field:
             for i in row:
                 add = '2' if i == -1 else str(i)
                 text += add
         return text