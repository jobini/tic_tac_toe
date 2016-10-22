from classes import *
from random import random

def main():
    print ""
    mode = which_mode()
    if mode == 'p':
        print ""
        p1_name = raw_input("Enter Player 1 (X) name: ")
        p2_name = raw_input("Enter Player 2 (O) name: ")

        p1 = Player('X',p1_name)
        p2 = Player('O',p2_name)
    else:
        if random() < 0.5:
            print ""
            p1_name = raw_input("Enter Player (X) name: ")
            p1 = Player('X',p1_name)
            p2 = Computer('O',"Computer")
        else:
            print ""
            p2_name = raw_input("Enter Player (O) name: ")
            p1 = Computer('X',"Computer")
            p2 = Player('O',p2_name)


    players = {0:p1,1:p2}

    g = Grid()
    g.display()

    i = 0

    while (not g.win() and not g.draw()):
        pos = players[i%2].ask_action()
        if g.is_valid(pos):
            players[i%2].play(pos,g)
            i += 1
            g.display()

    if g.win():
        if g.row_win()[0]:
            print "{0} wins!".format(players[g.row_win()[1] - 1].name)
        elif g.column_win()[0]:
            print "{0} wins!".format(players[g.column_win()[1] - 1].name)
        else:
            print "{0} wins!".format(players[g.diagonal_win()[1] - 1].name)

        play_again()
    else:
        print "Game is a draw!"
        print ""
        play_again()

def play_again():
    inp = raw_input("Play new game? [y]: ")
    if inp == 'y':
        Grid.played_pos = set()
        Player.p_num = 1
        main()

def which_mode():
    mode = raw_input("Human mode[p] or Computer mode[c]: ")
    if mode not in ['p','c']:
        print "Invalid mode! Try again."
        which_mode()
    else:
        return mode

main()
