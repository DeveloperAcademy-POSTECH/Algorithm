def solution(answers):
    result = []
    n = len(answers)
    first = []
    second = []
    third = []
    first_score = 0
    second_score = 0
    third_score = 0
    repeat_case1 = [1, 2, 3, 4, 5]
    repeat_case2 = [1, 3, 4, 5]
    repeat_case3 = [3, 1, 2, 4, 5]

    if n % len(repeat_case1) == 0:
        first = repeat_case1 * (n // 5)
    else:
        first = repeat_case1 * (n // 5) + repeat_case1[0: n % 5]

    for i in range(n):
        if i % 2 == 0:
            second.append(2)
        else:
            second.append(repeat_case2[(i % 8) // 2])

    for i in range(n // 2):
        third.append(repeat_case3[i % 5])
        third.append(repeat_case3[i % 5])
    if n % 2 == 1:
        third.append(repeat_case3[(n // 2 + 1) % 5 - 1])

    for i in range(n):
        if answers[i] == first[i]: first_score += 1
        if answers[i] == second[i]: second_score += 1
        if answers[i] == third[i]: third_score += 1

    max_score = max(first_score, second_score, third_score)
    if first_score == max_score: result.append(1)
    if second_score == max_score: result.append(2)
    if third_score == max_score: result.append(3)
    return result