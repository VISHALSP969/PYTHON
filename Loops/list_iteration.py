list1 = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

for s in list1:
    print(s)

for s in list1:
    print(s[:1])

for idx, s in enumerate(list1):
    print("%s has an index of %d" % (s, idx))

# Iterate over sub-list
for i in range(2, 4):
    print("list1 at %d contains %s" % (i, list1[i]))

for s in list1[1::2]:
    print(s)
