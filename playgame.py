import gamemodel, AIModel

made_ai_moves = [[],[]]

def print_field(field):
    for row in field:
        print (str(row) + "\n")

def ai_move(game, player):
    row, column = AIModel.get_best_move(game.field)
    game.field[int(row)][int(column)] = player
    print_field(game.field)

    #save made moves
    made_ai_moves[player].append((game.field, (row,column)))

def user_move(game, player):
    valid = False
    while(not valid):
        print("row between 0 and 2: ")
        row = input()
        print("column between 0 and 2: ")
        column = input()
        if gamemodel.move_is_valid((int(row), int(column)), game):
            game.field[int(row)][int(column)] = player
            print_field(game.field)
            valid = True
        else:
            print("No valid move. please choose again.")


#game modes - ai vs ai for training, user vs ai for playing
def ai_vs_ai(game):
    while(gamemodel.getWinner(game) == -1):
        ai_move(game, game.player)
        game.player = 1 - game.player
    return gamemodel.getWinner(game)

def ai_vs_user(game, starter):
    while (gamemodel.getWinner(game) == -1):
        if starter == 1:
            game.player = 1;
        ai_move(game, game.player) if game.player == 0 else user_move(game, game.player)
        game.player = 1 - game.player
    return gamemodel.getWinner(game)

def user_vs_user(game):#for testing
    while(gamemodel.getWinner(game) == -1):
        user_move(game, game.player)
        game.player = 1 - game.player
    return gamemodel.getWinner(game)


def startgame(mode):
    game = gamemodel.game()
    starter = 0 #0-> ai, 1 ->human

    if mode == 0:
        winner = ai_vs_ai(game)
    elif mode == 1:
        winner = ai_vs_user(game,starter)
    else:
        winner = user_vs_user(game)

    print("The winner is player ",winner)
    if(mode == 0 or mode ==1):
        AIModel.evaluateGame(made_ai_moves, winner)


#main loop
playmode = 2
startgame(playmode)

