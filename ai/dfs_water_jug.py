from collections import deque

def is_goal(state, goal):
    return state == goal

def get_successors(state, capA, capB):
    a, b = state
    successors = []
    successors.append((capA, b))
    successors.append((a, capB))
    successors.append((0, b))
    successors.append((a, 0))
    pour = min(a, capB - b)
    successors.append((a - pour, b + pour))
    pour = min(b, capA - a)
    successors.append((a + pour, b - pour))
    return successors

def dfs(capA, capB, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}
    while stack:
        state = stack.pop()
        if state in visited:
            continue
        visited.add(state)
        if is_goal(state, goal):
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]
        for succ in get_successors(state, capA, capB):
            if succ not in visited:
                parent[succ] = state
                stack.append(succ)
    return None

capA = 4
capB = 3
start = (0, 0)
goal = (2, 0)

path = dfs(capA, capB, start, goal)
print(path)
