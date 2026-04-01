import heapq

goal = (1,2,3,4,5,6,7,8,0)

moves = {
    0:[1,3], 1:[0,2,4], 2:[1,5],
    3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8],
    6:[3,7], 7:[4,6,8], 8:[5,7]
}

def h(s):  # Manhattan distance
    d = 0
    for i,v in enumerate(s):
        if v != 0:
            j = goal.index(v)
            d += abs(i//3 - j//3) + abs(i%3 - j%3)
    return d

def neighbors(s):
    res = []
    z = s.index(0)
    for m in moves[z]:
        ns = list(s)
        ns[z], ns[m] = ns[m], ns[z]
        res.append(tuple(ns))
    return res

def astar(start):
    pq = []
    heapq.heappush(pq, (0, start))
    parent = {start: None}
    g = {start: 0}

    while pq:
        _, s = heapq.heappop(pq)
        if s == goal:
            path = []
            while s:
                path.append(s)
                s = parent[s]
            return path[::-1]

        for ns in neighbors(s):
            ng = g[s] + 1
            if ns not in g or ng < g[ns]:
                g[ns] = ng
                heapq.heappush(pq, (ng + h(ns), ns))
                parent[ns] = s

    return None

def show(s):
    print(s[0:3])
    print(s[3:6])
    print(s[6:9])
    print()

start = (1,2,3,4,0,6,7,5,8)
sol = astar(start)

print("Solution steps:", len(sol)-1)
for s in sol:
    show(s)
