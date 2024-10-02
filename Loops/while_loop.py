import cmath

a = 10
while True:
    a = a - 1
    print(a)
    if a < 7:
        break
print("Done")

i = 0
while i < 4:
    print(i)
    i = i + 1

complex_num=cmath.sqrt(-1)
while complex_num:
    print(complex_num)
    break

while True:
    print("Infinite loop")