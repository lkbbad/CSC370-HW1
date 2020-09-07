import eightpuzzle
import heapq
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

if __name__ == '__main__':
    h1_nodes = []
    h2_nodes = []
    h1_depth = []
    h2_depth = []
    h1_branching = []
    h2_branching = []
    for x in range(NUMBER_OF_TRIALS):
        puzzle = eightpuzzle.EightPuzzle()
        initState = eightpuzzle.initTiles(puzzle)
        # print(initState.state)
        #Running a_star with both h1 and h2
        heuristics = [h1, h2]

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
                else:
                    h2_nodes.append(nodes_visited)
                    h2_depth.append(next_node.g)
                    if next_node.g != 0:
                        h2_branching.append(nodes_visited / next_node.g)
                    else:
                        h2_branching.append(0)
                # print("Depth: ", next_node.g)
                # print("-----------------")


    df = pandas.DataFrame(data={"h1 branching factor" : h1_branching, "h1 depth": h1_depth, "h1 nodes visited": h1_nodes, "h2 branching factor" : h2_branching, "h2 depth": h2_depth, "h2 nodes visited": h2_nodes})
    df.to_csv("./fixed_heuristics.csv", sep=',',index=False)
    
#    goal = eightpuzzle.EightPuzzle()
#
#    puzzle = eightpuzzle.EightPuzzle()
#    puzzle.state = [[7,2,4],[5,0,6],[8,3,1]]
#    h1 = h1(puzzle, goal)
#    h2 = h2(puzzle, goal)
#    print(h1, h2)

    # plt.plot(h1_depth, h1_nodes, 'r^', h2_depth, h2_nodes, 'bs')
    # plt.show()

