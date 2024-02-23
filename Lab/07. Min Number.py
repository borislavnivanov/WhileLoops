import sys

min_number = sys.maxsize

while True:
    text = input()
    if text == 'Stop':
        break
    else:
        if min_number > (int(text)):
            min_number = int(text)

print(min_number)
