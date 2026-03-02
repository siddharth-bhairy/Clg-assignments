import heapq

GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def manhattan_distance(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = GOAL_STATE.index(state[i])
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_pos, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)

    for move in MOVES[zero_index]:
        new_state = list(state)
        new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
        neighbors.append(tuple(new_state))

    return neighbors


def a_star(start_state):
    open_list = []
    heapq.heappush(open_list, (0, 0, start_state))

    came_from = {}
    g_cost = {start_state: 0}

    while open_list:
        _, current_g, current_state = heapq.heappop(open_list)

        if current_state == GOAL_STATE:
            return reconstruct_path(came_from, current_state)

        for neighbor in get_neighbors(current_state):
            tentative_g = current_g + 1

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + manhattan_distance(neighbor)
                heapq.heappush(open_list, (f_cost, tentative_g, neighbor))
                came_from[neighbor] = current_state

    return None


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    solution = a_star(start_state)

    if solution:
        print("Solution found in", len(solution) - 1, "moves\n")
        for step in solution:
            print_state(step)
    else:
        print("No solution found.")