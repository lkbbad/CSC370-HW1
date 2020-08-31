import sys
import copy
import math
import random

class EightPuzzle():
    def __init__(self):
        #self.state = [[[0], [1], [2]], [[3], [4], [5]], [[6], [7], [8]]]
        self.state = [[1, 2, 0], [3, 4, 5], [6, 7, 8]]
        self.x = self.get_blank_index()[0]
        self.y = self.get_blank_index()[1]

    def get_blank_index(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == 0:
                    x = j
                    y = i
        return (x,y)

    def neighbors(self):
        list = []
        # blank = self.get_blank_index()
        # x = blank[0]
        # y = blank[1]
        x = self.x
        y = self.y
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

    def initTiles(self):
        direction = 0
        # blank = self.get_blank_index()
        # x = blank[0]
        # y = blank[1]
        print(self.state)
        for i in range(0, 1):
            direction = random.randrange(0, 2, 1)
            if (direction == 0 and self.x > 0):
                self.state[self.y][self.x] = self.state[self.y][self.x-1] # move right the tile to the left of space
                self.state[self.y][self.x-1] = 0
            print(self.state)
            elif (direction == 1 and self.y > 0):
                self.state[self.y][self.x] = self.state[self.y][self.x+1] # move right the tile to the left of space
                self.state[self.y][self.x+1] = 0
            print(self.state)


if __name__ == '__main__':
   puzzle = EightPuzzle()
   print(puzzle.x)
   print(puzzle.y)
   puzzle.neighbors()
   puzzle.initTiles()
    