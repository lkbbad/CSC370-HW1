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

if __name__ == '__main__':
    puzzle = eightpuzzle.EightPuzzle()
    initState = eightpuzzle.initTiles(puzzle)
    print(initState)
    print(h1(initState))