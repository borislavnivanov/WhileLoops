change_inp = float(input())

count = 0
change = int(change_inp * 100)
nominals = [200, 100, 50, 20, 10, 5, 2, 1]

n = 0
current = 0
while change > 0:
    current = nominals[n]
    count += change // current
    change -= (change // current) * current
    n += 1

print(count)
