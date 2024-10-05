# anonymous function / lambda function

from functools import reduce

sum = lambda x, y: x + y

print(sum(10, 20))

numbers = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)

points = [(1, 2), (3, 1), (5, 0)]
points_sorted = sorted(points, key=lambda x: x[1])
print(points_sorted)


def make_incrementor(n):
    return lambda x: x + n


# lambda inside another function
inc = make_incrementor(10)
print(inc(5))
print(inc(50))
