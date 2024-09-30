# set operations returns new set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}

set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)
print(set3)

set3 = set1.difference(set2)
print(set3)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set1 |= set2
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set1 &= set2
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set1 -= set2
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set1 ^= set2
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set1.update(set2)
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set1.intersection_update(set2)
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set1.difference_update(set2)
print(set1)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set1.symmetric_difference_update(set2)
print(set1)