import random
import parentAI

#structure in weights:
#gamestate, move, playernr, weight

class AI(parentAI.Parent_AI):

    def __init__(self, game):
        parentAI.Parent_AI.__init__(self, game)

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
                    w = float(field[3])-(amount/2) if result == 't' else w #tie not that bad as loose
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

        best_move = valid_moves[random.randrange(0, len(valid_moves))]
        best_move_value = -1000000
        for move in valid_moves:
            move_str = str(move[0])+str(move[1])
            for node in relevantNodes:
                if move_str == node[1]:
                    if float(node[3]) > best_move_value:
                        best_move = move
                        best_move_value = float(node[3])
        return best_move


#TODO: always ties against herself, but against human really bad
#more criteria?
#evaluation witout given field neccessary?
#probably learn by playing against human