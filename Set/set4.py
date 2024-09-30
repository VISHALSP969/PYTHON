# set1={{1,2},{3,4}}      # Type error, unhashable type
# print(set1)

set2={frozenset({1,2}),frozenset({3,4})}
print(set2)
