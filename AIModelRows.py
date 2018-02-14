import random
import parentAI

#structure in weights:
#row/column/diagonal 3-tupel, field(0/1/2), playernr, weight

class AI(parentAI.Parent_AI):

    def __init__(self, game):
        parentAI.Parent_AI.__init__(self, game)

    def evaluate(self, made_moves, result, player):
        pass

    def get_best_move(self, current_field):
        pass