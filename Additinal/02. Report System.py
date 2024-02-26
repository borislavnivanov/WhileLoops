goal = int(input())

passes_count = 1

transactions_cash = 0
amount_cash = 0
transactions_card = 0
amount_card = 0

total_collected = 0

while goal > total_collected:
    order = input()

    if order == "End":
        print("Failed to collect required money for charity.")
        break

    transaction_amount = int(order)

    if passes_count % 2 == 0:
        if transaction_amount < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            transactions_card += 1
            amount_card += transaction_amount
    else:
        if transaction_amount > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            transactions_cash += 1
            amount_cash += transaction_amount

    total_collected = amount_card + amount_cash
    passes_count += 1

else:
    print(f"Average CS: {amount_cash / transactions_cash:.2f}\nAverage CC: {amount_card / transactions_card:.2f}")
