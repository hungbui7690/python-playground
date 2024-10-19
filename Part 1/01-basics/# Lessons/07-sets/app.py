# sets - unordered & unique elements
ingredients = {"tofu", "tofu", "avocado", "cherries", "pasta"}
print(ingredients)

# turn a list into a set
scores = set([100, 25, 38, 100, 27])
print(scores)

# add and remove methods
ingredients.add("tomato")
ingredients.remove("cherries") # raise error if not in set
ingredients.discard("apple")

print(ingredients)

# joining sets -> union
set_one = {1, 2, 3}
set_two = {3, 4, 5}

union_set = set_one.union(set_two)
print(union_set)

# intersection -> set of common elements
int_set = set_one.intersection(set_two)
print(int_set)

# frozen (immutable) sets
ages = frozenset([19, 21, 35, 25])
print(ages)