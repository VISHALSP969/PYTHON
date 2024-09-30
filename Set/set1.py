# Operations on sets

# With other sets
# Intersection
print({1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}))
print({1, 2, 3, 4, 5} & {3, 4, 5, 6})

# Union
print({1, 2, 3, 4, 5}.union({3, 4, 5, 6}))
print({1, 2, 3, 4, 5} | {3, 4, 5, 6})

# Difference
print({1, 2, 3, 4}.difference({2, 3, 4, 5}))
print({1, 2, 3, 4} - {2, 3, 4, 5})

# Symmetric difference
print({1, 2, 3, 4}.symmetric_difference({3, 4, 5}))
print({1, 2, 3, 4} ^ {3, 4, 5})

# Superset check
print({1, 2}.issuperset({1, 2, 3}))
print({1, 2} >= {1, 2, 3})

# Subset check
print({1, 2}.issubset({1, 2, 3}))
print({1, 2} <= {1, 2, 3})

# Disjoint check
print({1, 2}.isdisjoint({3, 4}))
print({1, 2}.isdisjoint({1, 4}))

# With single elements
# Existence check
print(2 in {1, 2, 3})
print(4 in {1, 2, 3})
print(4 not in {1, 2, 3})

# Add and Remove
s = {1, 2, 3}
print(s)
s.add(4)
print(s)

s.discard(3)
s.discard(5)
print(s)

s.remove(2)
# s.remove(5)     # Ket error
print(s)
