# Wumpus World Simulator using Propositional Logic and Forward Chaining

# Wumpus World using Propositional Logic and Forward Chaining

SIZE = 4

# World setup
pits = {(1, 3), (3, 3)}
wumpus = (2, 3)
gold = (4, 4)

# Agent position
agent = (1, 1)

# Knowledge Base
visited = set()
safe = {(1, 1)}

possible_pits = {
    (r, c)
    for r in range(1, SIZE + 1)
    for c in range(1, SIZE + 1)
    if (r, c) != (1, 1)
}

possible_wumpus = possible_pits.copy()


# Find neighboring cells
def neighbors(cell):
    r, c = cell

    result = []

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr = r + dr
        nc = c + dc

        if 1 <= nr <= SIZE and 1 <= nc <= SIZE:
            result.append((nr, nc))

    return result


# Perceive the environment
def perceive(cell):

    breeze = any(n in pits for n in neighbors(cell))
    stench = any(n == wumpus for n in neighbors(cell))
    glitter = cell == gold

    return breeze, stench, glitter


# Forward Chaining
def forward_chaining():

    changed = True

    while changed:

        changed = False

        for cell in visited:

            breeze, stench, glitter = perceive(cell)

            # Rule 1: No breeze means no neighboring pit
            if not breeze:

                for n in neighbors(cell):

                    if n in possible_pits:
                        possible_pits.remove(n)
                        changed = True

            # Rule 2: No stench means no neighboring Wumpus
            if not stench:

                for n in neighbors(cell):

                    if n in possible_wumpus:
                        possible_wumpus.remove(n)
                        changed = True

        # Rule 3: Mark cells safe
        for r in range(1, SIZE + 1):
            for c in range(1, SIZE + 1):

                cell = (r, c)

                if (cell not in possible_pits and
                    cell not in possible_wumpus):

                    if cell not in safe:
                        safe.add(cell)
                        changed = True


# Display percepts
def show_percepts(cell):

    breeze, stench, glitter = perceive(cell)

    print("\nAgent at:", cell)
    print("Breeze:", breeze)
    print("Stench:", stench)
    print("Glitter:", glitter)


# Display knowledge
def show_knowledge():

    print("\nSafe cells:", sorted(safe))
    print("Visited cells:", sorted(visited))


# Main Agent Program
def explore_world():

    global agent

    print("===== WUMPUS WORLD =====")
    print("Grid Size:", SIZE, "x", SIZE)
    print("Starting Position:", agent)

    while True:

        # Visit current cell
        visited.add(agent)

        # Perceive environment
        show_percepts(agent)

        breeze, stench, glitter = perceive(agent)

        # Check gold
        if glitter:
            print("\nGOLD FOUND!")
            print("Agent successfully completed the mission.")
            break

        # Apply Forward Chaining
        forward_chaining()

        show_knowledge()

        # Find unvisited safe cells
        available = sorted(safe - visited)

        if not available:
            print("\nNo more safe cells to explore.")
            print("Mission stopped.")
            break

        # Select next safe cell
        next_cell = available[0]

        print("\nMoving to safe cell:", next_cell)

        agent = next_cell

        # Safety check
        if agent in pits:
            print("Agent fell into a pit!")
            break

        if agent == wumpus:
            print("Agent encountered the Wumpus!")
            break


# Run program
explore_world()