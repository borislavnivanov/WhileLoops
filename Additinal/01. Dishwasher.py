bottles_det = int(input()) * 750

counter = 1
dishes = 0
pots = 0
detergent_used = 0

while True:
    terminal_read = input()

    if terminal_read == "End":
        print(f'Detergent was enough!\n'
              f'{dishes} dishes and {pots} pots were washed.\n'
              f'Leftover detergent {bottles_det - detergent_used} ml.')
        break

    for_cleaning = int(terminal_read)

    if counter % 3 != 0:
        dishes += for_cleaning
        detergent_used += for_cleaning * 5

    else:
        pots += for_cleaning
        detergent_used += for_cleaning * 15

    counter += 1

    if detergent_used > bottles_det:
        print(f'Not enough detergent, {abs(bottles_det - detergent_used)} ml. more necessary!')
        break
