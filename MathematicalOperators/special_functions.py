import math
import cmath

c = 4
print(math.sqrt(c))
print(cmath.sqrt(c))

x = 8
print(math.pow(x, 1 / 3))
print(x**(1/3))

print(math.exp(0))
print(math.exp(1))

print(math.expm1(x))
print(math.exp(x)-1)

print(math.expm1(0))
print(math.exp(0)-1)

print(math.exp(1e-6)-1)
print(math.expm1(1e-6))
