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
    
    #making sure heuristic is consistent
    #never enters this??
    if (not(prev_state.h - curr_state.h <= curr_state.g)):
        curr_state.h = prev_state.h - curr_state.g
        h1 = prev_state.h - curr_state.g
            
    return h1

def goal_positions(tile):
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in range(0,3):
        for j in range(0,3):
            if goal_state[i][j] == tile:
                return (i,j)

def h2(curr_state,prev_state, goal_state):

    h2 = 0
    for i in range(0,3):
        for j in range(0,3):
            curr_pos = (i,j) #coordinates of current tile
            goal_pos = goal_positions(curr_state.state[i][j]) #coordinates of current tile in goal board
            manhattan_distance = abs(curr_pos[0] - goal_pos[0]) + abs(curr_pos[1] - goal_pos[1])
            
            h2 += manhattan_distance
        
    curr_state.h = h2
    
    #making sure heuristic is consistent
    #never enters this??
    if (not(prev_state.h - curr_state.h <= curr_state.g)):
        curr_state.h = prev_state.h - curr_state.g
        h2 = prev_state.h - curr_state.g
    return h2
    


if __name__ == '__main__':
    puzzle = eightpuzzle.EightPuzzle()
    initState = eightpuzzle.initTiles(puzzle)
    print(initState.state)
    #Running a_star with both h1 and h2
    heuristics = [h1, h2]
    
    for heuristic in heuristics:
    
    
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
            
            print(next_node)
            
            nodes_visited += 1
            if (next_node.state == goal.state):
                goal_found = True
                break
            neighbors = next_node.neighbors()
            for moves in neighbors:
                frontier.put((heuristic(moves[0], prev_node, goal) + moves[0].g, moves[0]))
            
        if (empty):
            print("No possible solutions using", heuristic, "as the heuristic.")
        
        if (goal_found):
            print("Found a solution using ", heuristic, "as the heuristic!")
            print("-----------------")
            print("Nodes visited: ", nodes_visited)
            print("Depth: ", next_node.g)
            print("-----------------")
