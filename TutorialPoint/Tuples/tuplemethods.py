tup1 = (1, 2, 3, 4, 5)
tup2 = ('abc', 'def')

# sum()
print(sum(tup1))
# length
print(len(tup1))

# max()
print(max(tup1))

# min()
print(min(tup1))

# tuple()
l = tuple([1, 2, 3])
print(l)

# sorted
tup = (8, 4, 6, 1, 3, 9)
print(sorted(tup))

# any()
tup = (False, 1, False, 2, 3)
print(any(tup))

# all()
tup = (False, 1, False, 2, 3)
print(all(tup))
tup = (1, 2, 3)
print(all(tup))

# count()
tup = (1, 2, 3, 1, 2, 4, 5)
print(tup.count(5))
print(tup.count(1))

# index()
print(tup.index(5))
