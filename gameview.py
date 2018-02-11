# Anfang
import sys
from tkinter import *


def callback00(fields, player):
    fields[0][0].config(text=player)
def callback01(fields, player):
    fields[0][1].config(text=player)
def callback02(fields, player):
    fields[0][2].config(text=player)
def callback10(fields, player):
    fields[1][0].config(text=player)
def callback11(fields, player):
    fields[1][1].config(text=player)
def callback12(fields, player):
    fields[1][2].config(text=player)
def callback20(fields, player):
    fields[2][0].config(text=player)
def callback21(fields, player):
    fields[2][1].config(text=player)
def callback22(fields, player):
    fields[2][2].config(text=player)


def init_field(new, gamestate):
    root = Tk(className="Tic Tac Toe")
    root.resizable(0,0)

    fields = [[],[],[]]
    for i in range(0,3):
        for j in range(0,3):
            command = "cmd%d%d",i,j
            f = Button(root, text = "-1", width=10, height = 5, bg = "white")

            #callbacks
            # if i == 0 and j ==0:
            #     f.config(command = lambda: callback00(fields, player))
            # elif i == 0 and j == 1:
            #     f.config(command=lambda: callback01(fields, player))
            # elif i == 0 and j == 2:
            #     f.config(command=lambda: callback02(fields, player))
            # elif i == 1 and j == 0:
            #     f.config(command=lambda: callback10(fields, player))
            # elif i == 1 and j == 1:
            #     f.config(command=lambda: callback11(fields, player))
            # elif i == 1 and j == 2:
            #     f.config(command=lambda: callback12(fields, player))
            # elif i == 2 and j == 0:
            #     f.config(command=lambda: callback20(fields, player))
            # elif i == 2 and j == 1:
            #     f.config(command=lambda: callback21(fields, player))
            # elif i == 2 and j == 2:
            #     f.config(command=lambda: callback22(fields, player))

            f.grid(row=i,column=j)
            fields[i].append(f)


    if new == 0:
        draw_state(gamestate, fields)

    root.mainloop()

    return root, fields


def draw_state(gamestate, fields):
    for row in range(0,3):
        for column in range(0,3):
            state = gamestate[row][column]
            if state == 0:
                fields[row][column].config(text = "0")
            elif state == 1:
                fields[row][column].config(text = "1")
            else:
                pass


init_field(0,[[0,0,0],[-1,-1,-1],[1,1,1]])