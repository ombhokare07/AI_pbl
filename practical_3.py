# Simulate Hill-Climbing and Simulated Annealing for optimization (e.g., N-Queens, Sudoku minimization)

import random
import math

# Objective Function
def objective(x):
    return -(x - 5) ** 2 + 25


# Hill Climbing Algorithm
def hill_climbing():
    current = random.randint(0, 10)

    while True:
        neighbors = [current - 1, current + 1]

        # Find the best neighbor
        best = current

        for neighbor in neighbors:
            if 0 <= neighbor <= 10:
                if objective(neighbor) > objective(best):
                    best = neighbor

        # Stop if no better neighbor exists
        if best == current:
            break

        current = best

    return current, objective(current)


# Simulated Annealing Algorithm
def simulated_annealing():
    current = random.randint(0, 10)

    temperature = 100
    cooling_rate = 0.95

    while temperature > 0.1:

        neighbor = current + random.choice([-1, 1])

        if 0 <= neighbor <= 10:

            current_value = objective(current)
            neighbor_value = objective(neighbor)

            # Calculate difference
            difference = neighbor_value - current_value

            # Accept better or sometimes worse solution
            if difference > 0:
                current = neighbor
            else:
                probability = math.exp(difference / temperature)

                if random.random() < probability:
                    current = neighbor

        temperature *= cooling_rate

    return current, objective(current)


# Main Program
print("HILL CLIMBING")
x, value = hill_climbing()
print("Best x:", x)
print("Maximum Value:", value)

print("\nSIMULATED ANNEALING")
x, value = simulated_annealing()
print("Best x:", x)
print("Maximum Value:", value)