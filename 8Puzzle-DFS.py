import copy

initialState = [[3, 1, 2], [0, 4, 5], [6, 7, 8]]
goalState = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def printBoard(board):
    for row in board:
        print(row)

def getNextStates(currentState):
    nextStates = []

    for row in range(3):
        for col in range(3):
            if currentState[row][col] == 0:
                if row - 1 >= 0:
                    nextState = copy.deepcopy(currentState)
                    nextState[row][col], nextState[row-1][col] = nextState[row-1][col], nextState[row][col]
                    nextStates.append(nextState)

                if row + 1 <= 2:
                    nextState = copy.deepcopy(currentState)
                    nextState[row][col], nextState[row+1][col] = nextState[row+1][col], nextState[row][col]
                    nextStates.append(nextState)
                if col - 1 >= 0:
                    nextState = copy.deepcopy(currentState)
                    nextState[row][col], nextState[row][col-1] = nextState[row][col-1], nextState[row][col]
                    nextStates.append(nextState)
                if col + 1 <= 2:
                    nextState = copy.deepcopy(currentState)
                    nextState[row][col], nextState[row][col+1] = nextState[row][col+1], nextState[row][col]
                    nextStates.append(nextState)
                break
    
    return nextStates

def getSolution(currentState, goalState):
    visitedStates = []
    if goalState == currentState:
        print("Goal reached")
        printBoard(currentState)
        return
    stack = [currentState]

    while stack:
        currentState = stack.pop()
        print("Next state:")
        printBoard(currentState)
        visitedStates.append(currentState)
        for nextState in getNextStates(currentState):
            if goalState == nextState:
                print("Goal reached")
                printBoard(nextState)
                break
            if nextState not in visitedStates:
                stack.append(nextState)


    
print("Initial State")
printBoard(initialState)
getSolution(initialState, goalState)
        
