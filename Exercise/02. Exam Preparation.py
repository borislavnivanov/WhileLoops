bad_score_limit = int(input())

bad_problems = 0
problems_count = 0
problems_score = 0
last_problem_name = str()

while bad_problems != bad_score_limit:
    new_input = input()

    if new_input == "Enough":
        print(f'Average score: {problems_score / problems_count:.2f}\n'
              f'Number of problems: {problems_count}\n'
              f'Last problem: {last_problem_name}')
        break

    problem_name = new_input
    problem_score = int(input())

    problems_count += 1
    problems_score += problem_score
    last_problem_name = problem_name

    if problem_score <= 4:
        bad_problems += 1

else:
    print(f'You need a break, {bad_problems} poor grades.')
