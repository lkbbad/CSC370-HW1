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

def h1(curr_state, goal_state):
    
    h1 = 0
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            if (not(curr_state.state[i][j] == goal_state.state[i][j]) and not(curr_state.state[i][j] == 0)):
                h1 += 1
    
    curr_state.h = h1
            
    return h1

def goal_positions(tile):
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in range(0,3):
        for j in range(0,3):
            if goal_state[i][j] == tile:
                return (i,j)

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
    
def find_loc(curr_state, val):

    for i in range(0,3):
        for j in range(0,3):
            if(curr_state.state[i][j] == val):
                return (i,j)
    
    
def misplaced_tiles(curr_state, goal_state):
    misplaced_tiles = []
    
    for i in range(0,3):
        for j in range(0,3):
            if(not(curr_state.state[i][j] == goal_state.state[i][j]) and not(curr_state.state[i][j] == 0)):
                misplaced_tiles.append((i,j))
                
    return misplaced_tiles

#Implementing Relaxed Adjacency
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
    h1_branching = []
    h2_branching = []
    h3_branching = []
    for x in range(NUMBER_OF_TRIALS):
        puzzle = eightpuzzle.EightPuzzle()
        initState = eightpuzzle.initTiles(puzzle)
        # print(initState.state)
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

                # print(next_node)

                nodes_visited += 1
                if (next_node.state == goal.state):
                    goal_found = True
                    break
                neighbors = next_node.neighbors()
                for moves in neighbors:
                    frontier.put((heuristic(moves[0], goal) + moves[0].g, moves[0]))

            # if (empty):
                # print("No possible solutions using", heuristic, "as the heuristic.")

            if (goal_found):
                # print("Found a solution using ", heuristic, "as the heuristic!")
                # print("-----------------")
                # print("Nodes visited: ", nodes_visited)
                # print(heuristic)
                if h == 1:
                    h1_nodes.append(nodes_visited)
                    h1_depth.append(next_node.g)
                    if next_node.g != 0:
                        h1_branching.append(nodes_visited / next_node.g)
                    else:
                        h1_branching.append(0)
                if h == 2:
                    h2_nodes.append(nodes_visited)
                    h2_depth.append(next_node.g)
                    if next_node.g != 0:
                        h2_branching.append(nodes_visited / next_node.g)
                    else:
                        h2_branching.append(0)
                if h == 3:
                    h3_nodes.append(nodes_visited)
                    h3_depth.append(next_node.g)
                    if next_node.g != 0:
                        h3_branching.append(nodes_visited / next_node.g)
                    else:
                        h3_branching.append(0)
                
                # print("Depth: ", next_node.g)
                # print("-----------------")

    print(len(h1_branching), len(h1_depth), len(h1_nodes), len(h2_branching), len(h2_depth), len(h2_nodes), len(h3_branching), len(h3_depth), len(h3_nodes))
    df = pandas.DataFrame(data={"h1 branching factor" : h1_branching, "h1 depth": h1_depth, "h1 nodes visited": h1_nodes, "h2 branching factor" : h2_branching, "h2 depth": h2_depth, "h2 nodes visited": h2_nodes, "h3 branching factor" : h3_branching, "h3 depth": h3_depth, "h3 nodes visited": h3_nodes})
    df.to_csv("./3_heuristics.csv", sep=',',index=False)

#    goal = eightpuzzle.EightPuzzle()
#
#    puzzle = eightpuzzle.EightPuzzle()
#    puzzle.state = [[2,7,0],[5,4,3],[8,1,6]]
#    h3 = h3(puzzle, goal)
#    print(h3)

#     plt.plot(h1_depth, h1_nodes, 'r^', h2_depth, h2_nodes, 'bs')
#     plt.show()

