# Aim: Implement A* and Greedy Best-First Search for pathfinding on a 2D grid with obstacles.

import heapq

# Define the grid
grid = [
    ['S', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['.', '.', '.', '.', '.'],
    ['X', 'X', '.', 'X', '.'],
    ['.', '.', '.', '.', 'G']
]

ROWS = len(grid)
COLS = len(grid[0])

# Find start and goal positions
start = (0, 0)
goal = (4, 4)

# Manhattan Distance
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# Get valid neighboring cells
def get_neighbors(node):
    row, col = node

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if (0 <= new_row < ROWS and
            0 <= new_col < COLS and
            grid[new_row][new_col] != 'X'):

            neighbors.append((new_row, new_col))

    return neighbors


# Greedy Best First Search
def greedy_bfs(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    visited = set()

    while priority_queue:
        h, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic(neighbor, goal),
                     neighbor,
                     path + [neighbor])
                )

    return None


# A* Search
def astar(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    cost = {start: 0}

    while priority_queue:
        f, current, path = heapq.heappop(priority_queue)

        if current == goal:
            return path

        for neighbor in get_neighbors(current):
            new_cost = cost[current] + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost

                f = new_cost + heuristic(neighbor, goal)

                heapq.heappush(
                    priority_queue,
                    (f, neighbor, path + [neighbor])
                )

    return None


# Display path
def display_path(path):
    if path is None:
        print("No path found!")
        return

    result = [row.copy() for row in grid]

    for row, col in path:
        if result[row][col] not in ['S', 'G']:
            result[row][col] = '*'

    for row in result:
        print(' '.join(row))

    print("Path:", path)
    print("Path Cost:", len(path) - 1)


# Main program
print("GREEDY BEST FIRST SEARCH")
greedy_path = greedy_bfs(start, goal)
display_path(greedy_path)

print("\nA* SEARCH")
astar_path = astar(start, goal)
display_path(astar_path)