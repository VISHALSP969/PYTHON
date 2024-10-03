a = 60
b = 13

print(a, bin(a))
print(b, bin(b))

c = a & b
print(c, bin(c))

c = a | b
print(c, bin(c))

c = a ^ b
print(c, bin(c))

c = ~a
print(c, bin(c))

c = a << 2
print(c, bin(c))

c = a >> 2
print(c, bin(c))
