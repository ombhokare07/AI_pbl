# Parsing First-Order Logic Sentences and performing Unification, Forward Chaining, and Backward Chaining




# Facts
facts = {
    "American (West)",
    "Missile(M1)",
    "Owns (Nono, M1)",
    "Enemy (Nono, America)",
}

# Display Knowledge Base
print("===== INITIAL FACTS =====")
for fact in facts:
  print(fact)

# Forward Chaining
print("\n===== FORWARD CHAINING =====")

# Rule 1: Missile(x) -> Weapon(x)
if "Missile(M1)" in facts:
  facts.add("Weapon (M1)")
  print("Derived: Weapon (M1)")

# Rule 2: Missile(x) AND Owns(Nono, x) -> Sells(West, x, Nono)
if "Missile (M1)" in facts and "Owns (Nono, M1)" in facts:
  facts.add("Sells (West, M1, Nono)")
  print("Derived: Sells (West, M1, Nono)")

# Rule 3: Enemy(x, America) -> Hostile(x)
if "Enemy (Nono, America)" in facts:
  facts.add("Hostile (Nono)")
  print("Derived: Hostile (Nono)")

# Rule 4: American(x) AND Weapon(y) AND Sells(x,y,z) AND Hostile(z) -> Criminal(x)
if (
    "American (West)" in facts
    and "Weapon(M1)" in facts
    and "Sells (West, M1, Nono)" in facts
    and "Hostile (Nono)" in facts
):
  facts.add("Criminal (West)")
  print("Derived: Criminal (West)")

# Query
print("\n===== QUERY =====")
query = "Criminal (West)"

if query in facts:
  print(query, "= TRUE")
  print("West is a Criminal.")
else:
  print(query, "= FALSE")