import sys
import copy

class EightPuzzle():
    def __init__(self):
        #self.state = [[[0], [1], [2]], [[3], [4], [5]], [[6], [7], [8]]]
        self.state = [[3, 1, 2], [4, 0, 5], [6, 7, 8]]
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
            u.state[y][x] = u.state[y+1][x] # move tile below spac up
            u.state[y+1][x] = 0
            list.append((u,'u')) # add this move and board state to list
        print(list)
        return list


if __name__ == '__main__':
   puzzle = EightPuzzle()
   print(puzzle.blank_index)
   puzzle.neighbors()
#    for i in range(0,3):
#        for j in range(0,3):
#             if puzzle[i][j] == 0:
#                 x = j
#                 y = i
#     print((x,y))
    