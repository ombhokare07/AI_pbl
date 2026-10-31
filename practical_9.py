
# Building a Bayesian Network for a Weather-Picnic Domain and performing Inference using Bayes' Rule

from itertools import product

# Step 1: Define the Bayesian Network
nodes = {
    "Rain": {"parents": [], "cpt": {(): 0.3}},
    "Wind": {"parents": [], "cpt": {(): 0.4}},
    "Picnic": {
        "parents": ["Rain", "Wind"],
        "cpt": {
            (False, False): 0.90,
            (False, True): 0.60,
            (True, False): 0.20,
            (True, True): 0.05,
        },
    },
}

ORDER = ["Rain", "Wind", "Picnic"]


# Step 2: Joint Probability using the Chain Rule for Bayesian Networks
def prob_true(var, assignment):
  """Look up P(var = True | current values of its parents)."""
  parents = nodes[var]["parents"]
  key = tuple(assignment[p] for p in parents)
  return nodes[var]["cpt"][key]


def joint_probability(assignment):
  """Multiply each node's conditional probability together (chain rule)."""
  p = 1.0
  for var in ORDER:
    p_true = prob_true(var, assignment)
    p *= p_true if assignment[var] else (1 - p_true)
  return p


# Step 3: Inference by Enumeration Bayes Rule
def all_assignments(variables):
  """Yield every True/False combination for the given list of variables."""
  for values in product([True, False], repeat=len(variables)):
    yield dict(zip(variables, values))


def enumeration_ask(query_var, evidence):
  hidden_vars = [v for v in ORDER if v != query_var and v not in evidence]
  scores = {}
  for query_value in [True, False]:
    total = 0.0
    for hidden_assignment in all_assignments(hidden_vars):
      full_assignment = dict(hidden_assignment)
      full_assignment[query_var] = query_value
      full_assignment.update(evidence)
      total += joint_probability(full_assignment)
    scores[query_value] = total
  normaliser = sum(scores.values())
  return {k: v / normaliser for k, v in scores.items()}


def show(dist, var_name):
  print(f"P({var_name} = True) = {dist[True]:.4f}")
  print(f"P({var_name} = False) = {dist[False]:.4f}")


# Step 4: Run some queries
print("Query 1: What is the overall (prior) chance of a picnic?")
result1 = enumeration_ask("Picnic", {})
show(result1, "Picnic")

print("\nQuery 2: It is raining. What is the chance of a picnic?")
result2 = enumeration_ask("Picnic", {"Rain": True})
show(result2, "Picnic")

print(
    "\nQuery 3: We are told there was NO picnic. What is the chance it was"
    " raining?"
)
result3 = enumeration_ask("Rain", {"Picnic": False})
show(result3, "Rain")