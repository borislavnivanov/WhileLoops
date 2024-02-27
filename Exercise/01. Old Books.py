book_search = input()

book_count = 0

while True:
    book = input()

    if book == 'No More Books':
        print(f'The book you search is not here!\nYou checked {book_count} books.')
        break

    if book == book_search:
        print(f'You checked {book_count} books and found it.')
        break

    book_count += 1
