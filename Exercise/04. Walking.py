goal = 10_000
steps = 0

while steps < goal:
    var = input()

    if var == "Going home":
        steps += int(input())
        break

    else:
        steps += int(var)

if steps >= goal:
    print(f'Goal reached! Good job!\n{abs(goal - steps)} steps over the goal!')
else:
    print(f'{goal - steps} more steps to reach goal.')
