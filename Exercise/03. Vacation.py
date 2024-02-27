vacation_price = float(input())
budget = float(input())

days = 0
spending_days = 0

while budget < vacation_price and spending_days < 5:
    transaction_type = input()
    transaction_amount = float(input())

    days += 1

    if transaction_type == 'spend':
        budget -= transaction_amount
        spending_days += 1
        if budget < 0:
            budget = 0
    else:
        budget += transaction_amount
        spending_days = 0


if spending_days == 5:
    print(f'You can\'t save the money.\n{days}')
elif budget >= vacation_price:
    print(f'You saved the money for {days} days.')

