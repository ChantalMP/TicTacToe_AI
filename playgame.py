import gamemodel, AIModel, copy

made_ai_moves = [[],[]]

def print_field(field):
    for row in field:
        print (str(row) + "\n")

def field_to_text(field):
     text = ""
     for row in field:
         for i in row:
             add = '2' if i == -1 else str(i)
             text += add
     return text

def ai_move(game, player, ai):
    #print("AI move")
    row, column = ai.get_best_move(field_to_text(game.field))
    # save made moves
    tmp = field_to_text(game.field)
    made_ai_moves[player].append((tmp, (row, column)))

    game.field[int(row)][int(column)] = player
    #print_field(game.field)

def user_move(game, player):
    valid = False
    while(not valid):
        print("player ", player, ": row between 0 and 2: ")
        row = input()
        print("column between 0 and 2: ")
        column = input()
        if gamemodel.move_is_valid((int(row), int(column)), game):
            game.field[int(row)][int(column)] = player
            print_field(game.field)
            valid = True
        else:
            print("player ", player, ": No valid move. please choose again.")


#game modes - ai vs ai for training, user vs ai for playing
def ai_vs_ai(game, ai):
    while(gamemodel.getWinner(game) == -1):
        ai_move(game, game.player, ai)
        game.player = 1 - game.player
    return gamemodel.getWinner(game)

def ai_vs_user(game, starter, ai):
    if starter == 1:
        game.player = 1;
    while (gamemodel.getWinner(game) == -1):
        ai_move(game, game.player, ai) if game.player == 0 else user_move(game, game.player)
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

    ai = AIModel.AI(game)

    if mode == 0:
        winner = ai_vs_ai(game, ai)
    elif mode == 1:
        winner = ai_vs_user(game,starter, ai)
    else:
        winner = user_vs_user(game)

    if winner == 2:
        print ("That was a tie")
    else:
        print("The winner is player ",winner)
    if(mode == 0 or mode ==1):
        ai.evaluateGame(made_ai_moves, winner)
        ai.save_weights()


#main loop
playmode = 0
for i in range(0,100):
    print("Game ",i)
    startgame(playmode)
