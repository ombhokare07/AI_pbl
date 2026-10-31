# Plan Actions Using Classical Planning (STRIPS-like representation) for a Robot in a Grid World


from collections import deque

GRID_SIZE = 4
start = (1, 1)
goal = (4, 4)
obstacles = {(2, 2), (3, 2), (3, 3)}

moves = {
    "MoveUp": (0, 1),
    "MoveDown": (0, -1),
    "MoveLeft": (-1, 0),
    "MoveRight": (1, 0),
}


def is_valid(x, y):
  if x < 1 or x > GRID_SIZE:
    return False
  if y < 1 or y > GRID_SIZE:
    return False
  return True


def apply_action(state, action):
  x, y = state
  dx, dy = moves[action]
  new_x = x + dx
  new_y = y + dy

  if (new_x, new_y) in obstacles:
    return None

  if is_valid(new_x, new_y):
    return (new_x, new_y)
  return None


def find_plan(start, goal):
  queue = deque()
  queue.append((start, []))
  visited = {start}

  while queue:
    current_state, plan = queue.popleft()

    if current_state == goal:
      return plan

    for action in moves:
      new_state = apply_action(current_state, action)
      if new_state is not None and new_state not in visited:
        visited.add(new_state)
        new_plan = plan + [action]
        queue.append((new_state, new_plan))

  return None


plan = find_plan(start, goal)

print("Start State:", start)
print("Goal State:", goal)
print("Obstacles:", obstacles)

if plan:
  print("\nPlan Found:")
  for step, action in enumerate(plan, start=1):
    print("Step", step, ":", action)
  print("\nTotal Steps:", len(plan))
else:
  print("No plan found.")