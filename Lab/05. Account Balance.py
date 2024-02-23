current_account = 0.00

while True:
    word = input()
    if word == 'NoMoreMoney':
        break
    else:
        deposit = float(word)

    if deposit > 0:
        current_account += deposit
        print(f'Increase: {deposit:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {current_account:.2f}')
