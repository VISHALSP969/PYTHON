# Set operations using methods and builtins
a = {1, 2, 2, 3, 4}
b = {3, 3, 4, 4, 5}

print(a.intersection((b)))
print(a.union(b))
print(a.difference(b))
print(a.symmetric_difference(b))

c = {1, 2}
print(c.issubset(a))
print(c.issuperset(a))

d = {5, 6}
print(a.isdisjoint(b))
print(a.isdisjoint(d))
