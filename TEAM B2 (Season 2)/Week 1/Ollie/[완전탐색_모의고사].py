# https://school.programmers.co.kr/learn/courses/30/lessons/42840

import math

def solution(answers):
    guess = {
        0: [1,2,3,4,5]*math.ceil(10000/5),
        1: [2,1,2,3,2,4,2,5]*math.ceil(10000/8),
        2: [3,3,1,1,2,2,4,4,5,5,]*math.ceil(10000/10)
    }
    answer = [0, 0, 0]
    for i, a in enumerate(answers):
        for j in range(3):
            if guess[j][i] == a:
                answer[j] += 1
    max_score = max(answer)
    res = [i+1 for i in range(3) if answer[i] == max_score] 
    return res