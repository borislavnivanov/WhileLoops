import sys

max_number = -sys.maxsize

while True:
    text = input()
    if text == 'Stop':
        break
    else:
        if max_number < (int(text)):
            max_number = int(text)

print(max_number)
