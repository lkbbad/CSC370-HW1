import sys
import copy
import math
import random

TILECOUNT = 3
class EightPuzzle():
    def __init__(self):
        #self.state = [[[0], [1], [2]], [[3], [4], [5]], [[6], [7], [8]]]
        self.state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.blank_index = self.get_blank_index()

    def get_blank_index(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == 0:
                    x = j
                    y = i
        return (x,y)

    def neighbors(self):
        list = []
        blank = self.get_blank_index()
        x = blank[0]
        y = blank[1]
        if x > 0:
            r = copy.deepcopy(self) # make a copy of state
            r.state[y][x] = r.state[y][x-1] # move right the tile to the left of space
            r.state[y][x-1] = 0
            list.append((r,'r')) # add this move and board state to list
        if x < 2:
            l = copy.deepcopy(self) # make a copy of state
            l.state[y][x] = l.state[y][x+1] # move left the tile to the right of space
            l.state[y][x+1] = 0
            list.append((l,'l')) # add this move and board state to list
        if y > 0:
            d = copy.deepcopy(self) # make a copy of state
            d.state[y][x] = d.state[y-1][x] # move tile above space down
            d.state[y-1][x] = 0 
            list.append((d,'d')) # add this move and board state to list
        if y < 2:
            u = copy.deepcopy(self) # make a copy of state
            u.state[y][x] = u.state[y+1][x] # move tile below space up
            u.state[y+1][x] = 0
            list.append((u,'u')) # add this move and board state to list
        return list

    def __repr__(self):
        res = ''
        for row in range(3):
            res += ' '.join(map(str, self.state[row]))
            res += '\r\n'
        return res

if __name__ == '__main__':
   puzzle = EightPuzzle()
   print(puzzle.blank_index)
   
   print("Starting State: ")
   print(puzzle)
   
   iterations = random.randint(0, 30)
   print("Number of Iterations: ", iterations)

   for itr in range(iterations):
       moves = puzzle.neighbors()
       rand_index = random.randint(0, len(moves)-1)
       rand_move = moves[rand_index][0]
       print(rand_move)
       
   puzzle.state = rand_move.state
   print("Randomly Generated State: ")
   print(puzzle)
    