'''
Implementation of A* Algorithm to solve sliding 8-puzzle. 
Includes h1 - Hamming distance heuristic, h2 - Manhattan distance heuristic, h3 - Relaxed Adjacency heuristic.
Authors: Caroline Sigl and Lindy Bustabad
'''
import eightpuzzle
import heapq
import random
import copy
from queue import PriorityQueue
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas

NUMBER_OF_TRIALS = 50
goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

'''
The Hamming distance heuristic function (misplaced tiles).
'''
def h1(curr_state, goal_state):
    h1 = 0
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            if (not(curr_state.state[i][j] == goal_state.state[i][j]) and not(curr_state.state[i][j] == 0)):
                h1 += 1
    curr_state.h = h1     
    return h1

'''
Returns coordinates of current tile in goal state board.
'''
def goal_positions(tile):
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in range(0,3):
        for j in range(0,3):
            if goal_state[i][j] == tile:
                return (i,j)

'''
The Manhattan distance or city block distance heuristic function.
'''
def h2(curr_state, goal_state):
    h2 = 0
    for i in range(0,3):
        for j in range(0,3):
            if(not(curr_state.state[i][j] == 0)):
                curr_pos = (i,j) #coordinates of current tile
                goal_pos = goal_positions(curr_state.state[i][j]) #coordinates of current tile in goal board
                manhattan_distance = abs(curr_pos[0] - goal_pos[0]) + abs(curr_pos[1] - goal_pos[1])
            
                h2 += manhattan_distance
    curr_state.h = h2
    return h2
    
'''
Returns location of tile in current board state. 
'''
def find_loc(curr_state, val):
    for i in range(0,3):
        for j in range(0,3):
            if(curr_state.state[i][j] == val):
                return (i,j)

'''
Returns list of misplaced tiles in current board state.
'''    
def misplaced_tiles(curr_state, goal_state):
    misplaced_tiles = []
    for i in range(0,3):
        for j in range(0,3):
            if(not(curr_state.state[i][j] == goal_state.state[i][j]) and not(curr_state.state[i][j] == 0)):
                misplaced_tiles.append((i,j))       
    return misplaced_tiles

'''
The Relaxed Adjacency heuristic function.
'''
def h3(curr_state, goal_state):
    curr_cpy = copy.deepcopy(curr_state)
    misplaced = misplaced_tiles(curr_cpy, goal_state)  
    h3 = 0
    while(len(misplaced) > 0):
        loc_0 = find_loc(curr_cpy, 0)
        goal_0 = goal_positions(0)
        if(loc_0  == goal_0):
            x = 0
            x_loc = loc_0
            y_loc = misplaced[0]
            y = curr_cpy.state[y_loc[0]][y_loc[1]]         
            curr_cpy.state[x_loc[0]][x_loc[1]] = y
            curr_cpy.state[y_loc[0]][y_loc[1]] = x
        else:
            x = 0
            x_loc = loc_0         
            y = goal_state.state[x_loc[0]][x_loc[1]]
            y_loc = find_loc(curr_cpy, y)
            curr_cpy.state[x_loc[0]][x_loc[1]] = y
            curr_cpy.state[y_loc[0]][y_loc[1]] = x
        misplaced = misplaced_tiles(curr_cpy, goal_state)
        h3 += 1
    return h3    
        
if __name__ == '__main__':
    h1_nodes = []
    h2_nodes = []
    h3_nodes = []
    h1_depth = []
    h2_depth = []
    h3_depth = []
    for x in range(NUMBER_OF_TRIALS):
        puzzle = eightpuzzle.EightPuzzle()
        initState = eightpuzzle.initTiles(puzzle)
        #Running a_star with both h1 and h2
        heuristics = [h1, h2, h3]
        h = 0
        for heuristic in heuristics:
            h +=1
            #Initializing PriorityQueue frontier with neighbors
            frontier = PriorityQueue()
            frontier.put((0, initState))
            empty = False
            goal_found = False
            nodes_visited = 0
            #Establishing the goal state
            goal = eightpuzzle.EightPuzzle()
            #Creating any empty set to keep track of visited nodes
            explored_set = set()
            #Run a_star while frontier is full and goal hasn't been found
            while(not(empty) and not(goal_found)):
                empty = frontier.empty()
                if (empty):
                    break
                if (nodes_visited > 0):
                    prev_node = next_node
                next = frontier.get()
                next_node = next[1]
                #only add popped node to frontier if not yet explored
                if next_node in explored_set:
                    explored = True
                    while(explored):
                        next = frontier.get()
                        next_node = next[1]
                        if not(next_node in explored_set):
                            explored = False
                #add non-eplored node to explored set
                explored_set.add(next_node)
                if (nodes_visited == 0):
                    prev_node = next_node
                nodes_visited += 1
                if (next_node.state == goal.state):
                    goal_found = True
                    break
                neighbors = next_node.neighbors()
                for moves in neighbors:
                    frontier.put((heuristic(moves[0], goal) + moves[0].g, moves[0]))
            if (goal_found):
                if h == 1:
                    h1_nodes.append(nodes_visited)
                    h1_depth.append(next_node.g)
                if h == 2:
                    h2_nodes.append(nodes_visited)
                    h2_depth.append(next_node.g)
                if h == 3:
                    h3_nodes.append(nodes_visited)
                    h3_depth.append(next_node.g)
                    
                    
    df = pandas.DataFrame(data={"h1 depth": h1_depth, "h1 nodes visited": h1_nodes, "h2 depth": h2_depth, "h2 nodes visited": h2_nodes, "h3 depth": h3_depth, "h3 nodes visited": h3_nodes})
    df.to_csv("./3_heuristics.csv", sep=',',index=False)



