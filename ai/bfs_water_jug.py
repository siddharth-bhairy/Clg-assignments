def solve_water(c1, c2, target):
    queue = [[(0, 0)]]
    visited = {(0, 0)}

    while queue:
        path = queue.pop(0)
        u1, u2 = path[-1]

        if (u1, u2) == (target, 0):
            return path

        moves = [
            (c1, u2),
            (u1, c2),
            (0, u2),
            (u1, 0),
            (max(0, u1 - (c2 - u2)), min(c2, u2 + u1)),
            (min(c1, u1 + u2), max(0, u2 - (c1 - u1)))
        ]

        for move in moves:
            if move not in visited:
                visited.add(move)
                queue.append(path + [move])

    return None

print(solve_water(4, 3, 2))
