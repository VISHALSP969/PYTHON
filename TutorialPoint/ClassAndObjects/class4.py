a = 40  # create object <40>
b = a  # increase ref.count of <40>
c = [b]  # increase ref.count of <40>

print(a)
print(b)
print(c)

del a  # decrease ref.count of <40>
print(b)
print(c)

b = 100  # decrease ref.count of <40>
print(b)
print(c)

c[0] = -1
print(b)
print(c)
