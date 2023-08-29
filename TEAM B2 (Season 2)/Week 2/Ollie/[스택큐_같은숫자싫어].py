# 같은 숫자 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
from typing import List

def solution(arr: List[int]):
    result:List[int] = []
    lastNumber = arr.pop()
    
    while arr:
        currentNumber = arr.pop()
        if currentNumber != lastNumber:
            result.append(lastNumber)
            lastNumber = currentNumber
    
    result.append(lastNumber)
    
    return result[::-1]


## 이전의 나

def solution(arr):
    answer = []
    temp = -1
    for i in arr:
        if temp == i:
            continue
        answer.append(i)
        temp = i
    return answer