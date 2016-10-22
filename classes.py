from random import sample

class Grid:

    played_pos = set()

    def __init__(self):
        self.cells = [" " for i in range(0,9)]
        self.cell_states = [0 for i in range(0,9)]
        self.empty_win = False

    def display(self):
        for i in range(0,7,3):
            print " __ __ __"
            print "|{0} |{1} |{2} |\n".format(self.cells[i],self.cells[i+1],self.cells[i+2])

    def win(self):
        if (self.row_win()[0] or self.column_win()[0] or self.diagonal_win()[0]) and (not self.empty_win):
            return True
        else:
            return False

    def row_win(self):
        for i in range(0,7,3):
            if ((self.cells[i] == self.cells[i+1]) and (self.cells[i+1] == self.cells[i+2])):
                if self.cells[i] == " ":
                    self.empty_win = True
                else:
                    self.empty_win = False
                    return True,self.cell_states[i]

        return False,None

    def column_win(self):
        for i in range(0,3):
            if ((self.cells[i] == self.cells[i+3]) and (self.cells[i+3] == self.cells[i+6])):
                if self.cells[i] == " ":
                    self.empty_win = True
                else:
                    self.empty_win = False
                    return True,self.cell_states[i]

        return False,None

    def diagonal_win(self):
        if ((self.cells[0] == self.cells[4]) and (self.cells[4] == self.cells[8])):
            if self.cells[0] == " ":
                self.empty_win = True
            else:
                self.empty_win = False
                return True,self.cell_states[0]
        if ((self.cells[2] == self.cells[4]) and (self.cells[4] == self.cells[6])):
            if self.cells[2] == " ":
                self.empty_win = True
            else:
                self.empty_win = False
                return True,self.cell_states[2]

        return False,None

    def draw(self):
        if (not self.win() and 0 not in self.cell_states):
            return True
        else:
            return False

    def is_valid(self,pos):
        try:
            pos = int(pos)
        except:
            print "Invalid entry! Try again."
            return False
        if pos > 0 and pos < 10:
            if pos not in Grid.played_pos:
                return True
            else:
                print "Position already played! Try again."
                return False
        else:
            print "Positions must be from 1-9! Try again."
            return False


class Player:
    p_num = 1

    def __init__(self,token,name):
        self.token = token
        self.name = name
        self.number = Player.p_num
        Player.p_num += 1

    def play(self,pos,g):
        Grid.played_pos.add(int(pos))
        g.cells[int(pos)-1] = self.token
        g.cell_states[int(pos)-1] = self.number

    def ask_action(self):
        pos = raw_input("{0}'s turn (Player {1}): ".format(self.name,self.number))
        return pos

class Computer(Player):

    def ask_action(self):
        pos = sample({i for i in range(1,10)}.difference(Grid.played_pos),1)[0]
        print "{0}'s turn: {1}".format(self.name,pos)
        return pos
