initial_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def dfs(initial_state, goal_state):
    visited_states = []
    queue = []
    queue.append(initial_state)
    # print("l", queue)
    
    path = []

    while True:
        print("que", queue)
        print("visited", visited_states)
        current_state = queue[0]
        # print(current_state)
        del queue[0]
        visited_states.append(current_state)
        path.append(current_state)

        if goal_state == current_state:
            return path

        else:
            next_states = get_next_states(current_state)
            print("Nxt", next_states)
            for next_state in next_states:
                if next_state not in visited_states:
                    print("Not in visited")
                    queue.append(next_state)
                else:
                    print("in visited", next_state)
        break

def get_next_states(current_state):
    board = [[current_state[i] for i in range(j, j + 3)] for j in range(0, 9, 3)]
    # print("board", board)
    next_boards = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                print(row, col)
                if row - 1 > 0:
                    copy = board.copy()
                    copy[row][col] , copy[row - 1][col] = copy[row - 1][col], copy[row][col]
                    print("copy1", copy)
                    next_boards.append(copy)
                if row + 1 < 3:
                    copy = board.copy()
                    copy[row][col], copy[row + 1][col] = copy[row + 1][col], copy[row][col]
                    next_boards.append(copy)
                if col - 1 > 0:
                    copy = board.copy()
                    copy[row][col], copy[row][col - 1] = copy[row][col - 1], copy[row][col]
                    next_boards.append(copy)
                if col + 1 < 3:
                    copy = board.copy()
                    copy[row][col], copy[row][col + 1] = copy[row][col + 1], copy[row][col]
                    next_boards.append(copy)
    
    next_boards_flattened = []
    for board in next_boards:
        temp_board = []
        for row in board:
            for element in row:
                temp_board.append(element)
        next_boards_flattened.append(temp_board)
    
    return next_boards_flattened

def main():
    path = dfs(initial_state, goal_state)
    # print(path)
    # for step in path:
    #     print(step)

main()
