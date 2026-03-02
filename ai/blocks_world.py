import copy

def heuristic(state, goal):
    score = 0
    goal_stack = goal[0]

    for stack in state:
        for i in range(len(stack)):
            if i < len(goal_stack) and stack[i] == goal_stack[i]:
                score += 1
            else:
                break
    return score


def get_neighbors(state):
    neighbors = []

    for i in range(len(state)):
        if len(state[i]) == 0:
            continue

        for j in range(len(state)):
            if i != j:
                new_state = copy.deepcopy(state)
                block = new_state[i].pop()
                new_state[j].append(block)
                new_state = [stack for stack in new_state if stack]
                neighbors.append(new_state)

    return neighbors


def simple_hill_climbing(initial, goal):
    current = initial
    current_h = heuristic(current, goal)

    while True:
        neighbors = get_neighbors(current)
        next_state = None

        for neighbor in neighbors:
            h = heuristic(neighbor, goal)
            if h > current_h:
                next_state = neighbor
                current_h = h
                break

        if next_state is None:
            break

        current = next_state

    return current


def steepest_ascent(initial, goal):
    current = initial
    current_h = heuristic(current, goal)

    while True:
        neighbors = get_neighbors(current)
        best_neighbor = current
        best_h = current_h

        for neighbor in neighbors:
            h = heuristic(neighbor, goal)
            if h > best_h:
                best_neighbor = neighbor
                best_h = h

        if best_h == current_h:
            break

        current = best_neighbor
        current_h = best_h

    return current


if __name__ == "__main__":

    initial_state = [['C', 'A'], ['B']]
    goal_state = [['A', 'B', 'C']]

    print("Initial State:", initial_state)
    print("Goal State:", goal_state)

    print("\nSimple Hill Climbing Result:")
    print(simple_hill_climbing(initial_state, goal_state))

    print("\nSteepest Ascent Hill Climbing Result:")
    print(steepest_ascent(initial_state, goal_state))