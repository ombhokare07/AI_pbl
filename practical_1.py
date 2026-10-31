# Aim: Design and Implementation of a Problem-Solving Agent using Breadth-First Search and Depth-First Search Algorithms.

from collections import deque

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Breadth First Search
def bfs(start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(path + [neighbor])

    return None


# Depth First Search
def dfs(start, goal):
    visited = set()
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(path + [neighbor])

    return None


# Main program
start = 'A'
goal = 'F'

print("Breadth First Search (BFS):")
print("Path:", bfs(start, goal))

print("\nDepth First Search (DFS):")
print("Path:", dfs(start, goal))