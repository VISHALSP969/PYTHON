import operator

print(3%4)
print(10%2)
print(6%4)

print(operator.mod(3,4))
print(operator.mod(10,2))
print(operator.mod(6,4))

print(-9%7)
print(9%-7)
print(-9%-7)

quotient,remainder=divmod(9,4)
print(quotient,remainder)