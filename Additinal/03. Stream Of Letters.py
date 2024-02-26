word = str()
has_n_occurred = False
has_o_occurred = False
has_c_occurred = False
temp_word = str()

while True:
    read = input()

    if read == 'End':
        print(word)
        break

    if 65 <= ord(read) <= 90 or 97 <= ord(read) <= 122:

        if read == 'n' and not has_n_occurred:
            has_n_occurred = True
        elif read == 'o' and not has_o_occurred:
            has_o_occurred = True
        elif read == 'c' and not has_c_occurred:
            has_c_occurred = True
        else:
            temp_word += read

    if has_n_occurred and has_o_occurred and has_c_occurred:
        word += temp_word + ' '
        temp_word = ''
        has_c_occurred = False
        has_o_occurred = False
        has_n_occurred = False
