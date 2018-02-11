

try:
    weightfile = open("weights.txt", "r")
except FileNotFoundError:
    weightfile = open("weights.txt", "w")

if weightfile.mode == 'r':
    fl = weightfile.readlines()  # readlines reads the individual lines into a list
    for line in fl:
        for word in line.split():
            print(word)
