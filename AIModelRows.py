import random, math
import parentAI as p
from decimal import Decimal


#structure in weights:
#row/column/diagonal 3-tupel, field(0/1/2), playernr, weight



class AI(p.Parent_AI):

    def __init__(self, game):
        p.Parent_AI.__init__(self, game)
        self.init_weights()

    def init_weights(self):
        if self.weights == []:
            for player in ('0','1'):
                for first in ('0','1','2'):
                    for second in ('0','1','2'):
                        for third in ('0','1','2'):
                            for move in (0,1,2):
                                if (move == 0 and first == '2') or (move == 1 and second == '2') or (move == 2 and third == '2'):
                                    self.weights.append([first+second+third, player, move ,0.5])
            p.Parent_AI.save_weights(self)
            self.read_weights()
        else:
            pass

    def getRows(self, field_str, row, column):
        chosen_row = field_str[(row * 3):((row * 3) + 3)]
        chosen_column = field_str[column] + field_str[column + 3] + field_str[column + 6]
        chosen_diag1 = ""
        chosen_diag2 = ""
        if row == column == 1:
            chosen_diag1 = field_str[0] + field_str[4] + field_str[8]
            chosen_diag2 = field_str[2] + field_str[4] + field_str[6]
        elif row != 1 and column != 1:
            if row == column:
                chosen_diag1 = field_str[0] + field_str[4] + field_str[8]
            else:
                chosen_diag2 = field_str[2] + field_str[4] + field_str[6]

        return chosen_row, chosen_column, chosen_diag1, chosen_diag2

    def evaluate(self, made_moves, result, player):
        # move: (field, (row,column))
        movecount = len(made_moves)
        for move in range(0, movecount):
            fieldstr = made_moves[move][0]
            row = made_moves[move][1][0]
            column = made_moves[move][1][1]
            rowMove = column
            columnMove = row
            if row == column == 1:
                diag1Move = diag2Move = 1
            else:
                diag1Move = 0 if row == column == 1 else 2
                diag2Move = 0 if row == 0 and column == 2 else 2

            # convert in 3-tupel
            chosen_row, chosen_column, chosen_diag1, chosen_diag2 = self.getRows(fieldstr, row, column)
            tuples = [chosen_row, chosen_column, chosen_diag1, chosen_diag2]
            moves = [rowMove, columnMove, diag1Move, diag2Move]

            if result == 'w':
                amount = Decimal(((move + 1) / movecount)**2)
            elif result == 'l':
                amount = Decimal(-(((move + 1) / movecount)**2))
            else:
                amount = Decimal(-(((move + 1) / movecount))/4)

            #relevance of tuples:
            empty = {}
            for t in tuples:
                if t != '':
                    if t[0] == t[1] != '2' or t[0] == t[2] != '2' or t[1] == t[2] != '2':
                        empty.update({t:2.0})
                    else:
                        empty.update({t:1.0})

            for t in range(0,4):
                if tuples[t] != '': #empty string if diagonal dont exists
                    for entry in self.weights:
                        if entry[0] == tuples[t] and entry[1] == str(player) and entry[2] == str(moves[t]):
                            if (Decimal(entry[3]) == 0):
                                print("e: ", entry)
                            #old_weight = p.Parent_AI.rev_sigmoid(self, Decimal(entry[3]))
                            #tmp = Decimal(old_weight + amount*(Decimal(math.pow(empty[tuples[t]],6))))
                            #new_weight = p.Parent_AI.sigmoid(self, tmp)
                            old_weight = Decimal(entry[3])
                            new_weight = old_weight + amount*Decimal(math.pow(empty[tuples[t]],6))
                            if new_weight != 0.0 and new_weight != 1.0:
                                entry[3] = new_weight
                        if entry[0] == tuples[t] and entry[1] == str(1-player) and entry[2] == str(moves[t]):
                            if(entry[3]==0.0 or entry[3] == 1.0):
                                print("help: ", entry)
                            #old_weight = p.Parent_AI.rev_sigmoid(self, Decimal(entry[3]))
                            #tmp = Decimal(old_weight + amount*(Decimal(math.pow(empty[tuples[t]],6)))/2)
                            #new_weight = p.Parent_AI.sigmoid(self, tmp)
                            old_weight = Decimal(entry[3])
                            new_weight = old_weight + amount*Decimal(( math.pow(empty[tuples[t]],6))/2)
                            entry[3] = new_weight

    def get_best_move(self, current_field_str):
        valid_moves = self.get_valid_moves(self.game)
        if len(valid_moves) == 1:#dont search if only one move left
            return valid_moves[0]

        values = {}
        for move in valid_moves:
            # move = (row,column)
            test_row, test_column, test_diag1, test_diag2 = self.getRows(current_field_str, move[0], move[1])
            value = self.calc_value(move, test_row, test_column, test_diag1, test_diag2)
            values.update({value: move})

        key_of_best = max(values.keys())
        if key_of_best == 0.0:
            return valid_moves[random.randrange(0, len(valid_moves))]
        else:
            return values[key_of_best]

    def calc_value(self, move, test_row, test_column, test_diag1, test_diag2):
        row = move[0]
        column = move[1]
        rowMove = column
        columnMove = row
        if row == column == 1:
            diag1Move = diag2Move = 1
        else:
            diag1Move = 0 if row == column == 1 else 2
            diag2Move = 0 if row == 0 and column == 2 else 2
        moves = [rowMove, columnMove, diag1Move, diag2Move]
        tuples = [test_row, test_column, test_diag1, test_diag2]

        count = 0
        val = []
        ret_val = 0
        for i in range(0,4):
            if tuples[i] != '':
                count += 1
                for w in self.weights:
                    if w[0] == tuples[i] and w[1] == str(self.game.player) and w[2] == str(moves[i]):
                        val.append(Decimal(w[3]))
                        #ret_val += float(w[3])
                        break

        max_val = max(val)
        ret_val = 0
        for v in val:
            if v == max_val:
                ret_val += count*v
            else:
                ret_val += v
        return ret_val/count



