import eightpuzzle
import heapq
from queue import PriorityQueue


goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def h1(curr_state,prev_state, goal_state):
    
    h1 = 0
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            if (not(curr_state.state[i][j] == goal_state.state[i][j])):
                h1 += 1
    
    curr_state.h = h1
    
    if (not(prev_state.h - curr_state.h <= curr_state.g)):
        curr_state.h = prev_state.h - curr_state.g
        h1 = prev_state.h - curr_state.g
        
    curr_state.h = h1
    
    return h1

def goal_positions(tile):
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in range(0,3):
        for j in range(0,3):
            if goal_state[i][j] == tile:
                return (i,j)

def h2(initState):
    h2 = 0
    for i in range(0,3):
        for j in range(0,3):
            goal_pos = goal_positions(initState.state[i][j])
            # print("Goal: " + str(goal_pos))
            # print("Current: " + str((i,j)))
            res = tuple(map(lambda i, j: i - j, goal_pos, (i,j)))
            # print(res)
            res_x = abs(res[0])
            res_y = abs(res[1])
            if initState.state[i][j] != 0:
                manhattan_distance = res_x + res_y
            else:
                manhattan_distance = 0
            # print(manhattan_distance)
            h2 += manhattan_distance
    return h2
    
    

if __name__ == '__main__':
    puzzle = eightpuzzle.EightPuzzle()
    initState = eightpuzzle.initTiles(puzzle)
    print(initState.state)
    
    #Initializing PriorityQueue frontier with neighbors
    frontier = PriorityQueue()
    
    frontier.put((0, initState))
        
    empty = False
    goal_found = False
    nodes_visited = 0
    
    goal = eightpuzzle.EightPuzzle()
    explored_set = set()
        
    while(not(empty) and not(goal_found)):
        empty = frontier.empty()
        if (empty):
            break
        if (nodes_visited > 0):
            prev_node = next_node
            
        next = frontier.get()
        next_node = next[1]
        if next_node in explored_set:
            explored = True
            while(explored):
                next = frontier.get()
                next_node = next[1]
                if not(next_node in explored_set):
                    explored = False
                
                
        explored_set.add(next_node)
        
        if (nodes_visited == 0):
            prev_node = next_node
        
        print(next_node)
        
        nodes_visited += 1
        if (next_node.state == goal.state):
            goal_found = True
            break
        neighbors = next_node.neighbors()
        for moves in neighbors:
            frontier.put((h1(moves[0], prev_node, goal) + moves[0].g, moves[0]))
        
    if (empty):
        print("No possible solutions :(")
    
    if (goal_found):
        print("Found a solution!")
        print("-----------------")
        print("Nodes visited: ", nodes_visited)
        print("Depth: ", next_node.g)
        print("-----------------")
