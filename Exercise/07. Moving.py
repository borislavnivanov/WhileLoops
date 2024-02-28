apartment_width = int(input())
apartment_length = int(input())
apartment_height = int(input())

apartment_size = apartment_height * apartment_length * apartment_width

while apartment_size > 0:
    console_input = input()

    if console_input == "Done":
        print(f'{apartment_size} Cubic meters left.')
        break

    apartment_size -= int(console_input)
else:
    print(f'No more free space! You need {abs(apartment_size)} Cubic meters more.')
