import heapq

GOAL = (1,2,3,4,5,6,7,8,0)

# Allowed blank-tile moves by index
NEIGHBOR_INDEX = {
    0:[1,3], 1:[0,2,4], 2:[1,5],
    3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8],
    6:[3,7], 7:[4,6,8], 8:[5,7]
}

# Manhattan distance heuristic
def manhattan(state):
    total = 0
    for idx, value in enumerate(state):
        if value != 0:
            goal_index = GOAL.index(value)
            total += abs(idx//3 - goal_index//3) + abs(idx%3 - goal_index%3)
    return total

# Generate new states by sliding tiles
def get_next_states(state):
    next_states = []
    blank = state.index(0)

    for move in NEIGHBOR_INDEX[blank]:
        new_state = list(state)
        new_state[blank], new_state[move] = new_state[move], new_state[blank]
        next_states.append(tuple(new_state))

    return next_states

# A* Algorithm
def a_star(start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    parent = {start: None}
    g_cost = {start: 0}

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current == GOAL:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for nxt in get_next_states(current):
            new_cost = g_cost[current] + 1

            if nxt not in g_cost or new_cost < g_cost[nxt]:
                g_cost[nxt] = new_cost
                f_cost = new_cost + manhattan(nxt)
                heapq.heappush(priority_queue, (f_cost, nxt))
                parent[nxt] = current

    return None

# Display 3×3 board
def print_board(state):
    print(state[:3])
    print(state[3:6])
    print(state[6:])
    print()

# Run
start_state = (1,2,3,4,0,6,7,5,8)
solution = a_star(start_state)

print("Steps:", len(solution)-1)
for step in solution:
    print_board(step)
