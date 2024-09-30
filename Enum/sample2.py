from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3

# Enum are iterable
for c in Color:
    print(c)
