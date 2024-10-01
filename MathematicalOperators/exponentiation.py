import math
import operator

a, b = 2, 3
print(a ** b)

print(pow(2, 5))
print(operator.pow(10, 3))

a, b, c = 2, 3, 2
print(pow(a, b, c))     # (a**b)%c  - 0
