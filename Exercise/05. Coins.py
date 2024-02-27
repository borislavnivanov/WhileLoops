import math

change_inp = float(input())

change = abs(math.trunc(change_inp * 100))
count = 0
nominals = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

n = 0
while change > 0:
    if change >= nominals[n]:
        change -= nominals[n]
        count += 1
        n = -1
    n += 1

print(count)
