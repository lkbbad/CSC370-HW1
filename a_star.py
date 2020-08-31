import eightpuzzle

def h1(initState):
    h1 = 0
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            if initState.state[i][j] != count:
                # print(initState.state[i][j], count)
                if count != 0:
                    h1 += 1
            count += 1
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
    print(initState)
    print(h1(initState))
    print(h2(initState))