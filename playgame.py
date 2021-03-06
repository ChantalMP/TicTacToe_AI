import gamemodel, AIModelWholeField, AIModelRows

made_ai_moves = [[],[]]

ties = 0
a = 0
r = 0
p = False

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
    #save made moves for fieldAI
    tmp = field_to_text(game.field)
    made_ai_moves[player].append((tmp, (row, column)))

    game.field[int(row)][int(column)] = player
    if p:
        print_field(game.field)

def user_move(game, player):
    valid = False
    while(not valid):
        print("player ", player, ": row between 0 and 2: ")
        row = input()
        print("column between 0 and 2: ")
        column = input()
        if row not in ('0', '1', '2') or column not in ('0','1','2'):
            print("player ", player, ": No valid move. please choose again.")
            continue
        if gamemodel.move_is_valid((int(row), int(column)), game):
            game.field[int(row)][int(column)] = player
            print_field(game.field)
            valid = True
        else:
            print("player ", player, ": No valid move. please choose again.")

def random_move(game, player, ai):
    #print("random")
    row, column = ai.randomMove(game.field)
    game.field[int(row)][int(column)] = player
    #print_field(game.field)

def ai_vs_ai(game, ai):
    while (gamemodel.getWinner(game) == -1):
        ai_move(game, game.player, ai)
        game.player = 1 - game.player
    return gamemodel.getWinner(game)


#game modes - ai vs ai for training, user vs ai for playing
def rand_vs_ai(game, starter, ai):
    if starter == 1:
        game.player = 1;
    else:
        game.player = 0
    while(gamemodel.getWinner(game) == -1):
        ai_move(game, game.player, ai) if game.player == 0 else random_move(game, game.player, ai)
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

def startgame(mode, starter):
    global r, a, ties, p
    game = gamemodel.game()
    #starter = 0-> ai, 1 ->human

    #ai = AIModelWholeField.AI(game)
    ai = AIModelRows.AI(game)


    if mode == 0:
        p = False
        winner = ai_vs_ai(game, ai)
    elif mode == 1:
        p = True
        winner = ai_vs_user(game,starter, ai)
    elif mode == 2:
        p = False
        winner = rand_vs_ai(game, starter, ai)
    else:
        p = True
        winner = user_vs_user(game)

    if winner == 2:
        if p:
            print ("That was a tie")
        ties += 1

    else:
        if p:
            print("The winner is player ", winner)
        if winner == 0:
            a += 1
        else:
            r +=1

    if(mode == 0 or mode ==1 or mode == 2):
        ai.evaluateGame(made_ai_moves, winner)
        ai.save_weights()

#main loop
#first training

starter = 0
# for i in range(0,10):
#     print("round: ",i)
#     for i in range(0,250):
#         startgame(2, starter)
#         starter = 1 - starter
#
#     for i in range(0, 250):
#         startgame(0, starter)
#         starter = 1 - starter

#test:
# ties = a = r = 0
# for i in range(0,100):
#     startgame(2, starter)
#     starter = 1 - starter
# print("RANDOM: Ties: ", ties, "   AI: ", a, "   Random: ", r)
#
# ties = a = r = 0
# for i in range(0,100):
#     startgame(0, starter)
#     starter = 1 - starter
# print("RANDOM: Ties: ", ties, "   AI1: ", a, "   AI2: ", r)

for i in range(0,4):
    startgame(1,starter)
    starter = 1- starter