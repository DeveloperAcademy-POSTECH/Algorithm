#완전탐색_모의고사
def solution(answers):
    size = len(answers)

    tmp2 = [2,1,2,3,2,4,2,5]
    tmp3 = [3,3,1,1,2,2,4,4,5,5]

    student1 = [i % 5 + 1 for i in range(size)]
    student2 = [tmp2[i%len(tmp2)] for i in range(size)]
    student3 = [tmp3[i%len(tmp3)] for i in range(size)]

    answer = [0,0,0]
    result = []

    for i in range(size):
        if student1[i] == answers[i]:
            answer[0] += 1
        if student2[i] == answers[i]:
            answer[1] += 1
        if student3[i] == answers[i]:
            answer[2] += 1

    for i in range(3):
        if max(answer) == answer[i]:
            result.append(i+1)

    return result