#save game state and possible fields
class game:
    def __init__(self):
        self.field = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
        self.winner = -1
        self.player = 0

#winning conditions
def lines(field):
    for zeile in range(0, 3):
        if field[zeile][0] == field[zeile][1] == field[zeile][2]:
            if (field[zeile][0])!= -1:
                return field[zeile][0]
    return -1

def columns(field):
    for spalte in range(0, 3):
        if field[0][spalte] == field[1][spalte] == field[2][spalte]:
            if field[0][spalte] != -1:
                return field[0][spalte]
    return -1

def diagonals(field):
    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != -1:
        return field[0][0]
    elif field[0][2] == field[1][1] == field[2][0] and field[0][2] != -1:
        return field[0][2]
    else:
        return -1

#get winner
def getWinner(game):
    field = game.field
    ret = -1 if (lines(field) == -1 and columns(field) == -1 and diagonals(field) == -1) else max(lines(field),columns(field),diagonals(field))
    if ret == -1 and not moves_left(game):
        return 2
    return ret

def moves_left(game):
    for row in range(0,3):
        for column in range(0,3):
            if move_is_valid((row,column), game):
                return True
    return False;

#valid moves
def move_is_valid(move, game):
    #field: e.g (0,0), (0,1), ...
    field = game.field
    ret = True if field[move[0]][move[1]] == -1 else False
    return ret