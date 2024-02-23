name = input()

sum_grades = 0.00
grades = 1
fail = 0
program_grades = 12


# while True:
#     score = float(input())
#     if score < 4:
#         fail += 1
#         if fail >= 2:
#             print(f'{name} has been excluded at {grades} grade')
#             break
#         continue
#     grades += 1
#     sum_grades += score
#     if grades > 12:
#         average_score = sum_grades / 12
#         print(f'{name} graduated. Average grade: {average_score:.2f}')
#         break


while grades <= program_grades:
    score = float(input())
    if score < 4:
        fail += 1
        if fail == 2:
            print(f'{name} has been excluded at {grades} grade')
            break
        continue
    grades += 1
    sum_grades += score
    if grades > 12:
        average_score = sum_grades / 12
        print(f'{name} graduated. Average grade: {average_score:.2f}')

