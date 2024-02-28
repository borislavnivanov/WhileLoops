cake_x = int(input())
cake_y = int(input())

cake_pieces = cake_y * cake_x

while cake_pieces > 0:
    console_input = input()
    if console_input == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break

    cake_pieces -= int(console_input)

else:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
