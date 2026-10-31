# Solve a Constraint Satisfaction Problem (e.g., map coloring, sudoku) using Backtracking + Forward Checking


def is_valid(region, color, graph, assignment):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


# Backtracking Algorithm
def backtracking(graph, regions, colors, assignment):

    if len(assignment) == len(regions):
        return assignment.copy()

    # Select unassigned region
    region = next(r for r in regions if r not in assignment)

    for color in colors:

        if is_valid(region, color, graph, assignment):

            assignment[region] = color

            result = backtracking(
                graph, regions, colors, assignment
            )

            if result is not None:
                return result

            # Backtrack
            del assignment[region]

    return None


# Forward Checking Algorithm
def forward_checking(graph, regions, domains, assignment):

    if len(assignment) == len(regions):
        return assignment.copy()

    # Select unassigned region
    region = next(r for r in regions if r not in assignment)

    for color in domains[region]:

        if is_valid(region, color, graph, assignment):

            assignment[region] = color

            # Copy domains
            new_domains = {
                r: domains[r].copy() for r in regions
            }

            failed = False

            # Remove selected color from neighbors
            for neighbor in graph[region]:

                if neighbor not in assignment:

                    if color in new_domains[neighbor]:
                        new_domains[neighbor].remove(color)

                    # Check empty domain
                    if len(new_domains[neighbor]) == 0:
                        failed = True
                        break

            if not failed:

                result = forward_checking(
                    graph, regions, new_domains, assignment
                )

                if result is not None:
                    return result

            # Backtrack
            del assignment[region]

    return None


# Main Program
print("===== MAP COLORING CSP =====")

# Input number of regions
n = int(input("Enter number of regions: "))

regions = []

print("\nEnter region names:")

for i in range(n):
    region = input(f"Region {i+1}: ").strip()

    while not region or region in regions:
        print("Enter a non-empty, unique region name.")
        region = input(f"Region {i+1}: ").strip()

    regions.append(region)


# Create graph
graph = {region: [] for region in regions}

print("\nEnter neighboring regions.")
print("Enter neighbor names separated by spaces.")
print("Example: B C")

for region in regions:

    neighbors = input(
        f"Neighbors of {region}: "
    ).split()

    for neighbor in neighbors:

        if neighbor not in regions:
            print("Invalid region:", neighbor)
        elif neighbor != region:
            if neighbor not in graph[region]:
                graph[region].append(neighbor)

            if region not in graph[neighbor]:
                graph[neighbor].append(region)


# Input colors
colors = input(
    "\nEnter available colors separated by spaces: "
).split()

if not colors:
    print("No colors entered!")
    exit()


# Backtracking
print("\n===== BACKTRACKING =====")

result1 = backtracking(graph, regions, colors, {})

if result1:
    print("Solution Found:")
    for region, color in result1.items():
        print(region, ":", color)
else:
    print("No solution found!")


# Forward Checking
print("\n===== FORWARD CHECKING =====")

domains = {
    region: colors.copy() for region in regions
}

result2 = forward_checking(graph, regions, domains, {})

if result2:
    print("Solution Found:")
    for region, color in result2.items():
        print(region, ":", color)
else:
    print("No solution found!")