# https://school.programmers.co.kr/learn/courses/30/lessons/42842

import math

# yellow의 약수를 구하자. 약수 쌍에 2를 더한 것이 width, height가 된다.
# 얘를 1씩 빼고 2를 곱했을 때 brown이 된다면, 그것이 답.

# 약수를 효율적으로 구하기
# - 제곱근까지만 구한다.
# https://kbw1101.tistory.com/32

def solution(brown, yellow):
    pairs = getPairs(yellow)

    def isAnswer(i, j) -> bool:
        return brown == ((i - 1) + (j - 1)) * 2
    
    for width, height in pairs:
        if isAnswer(width, height):
            return [width, height]

def getPairs(number):
    return [ ((number//i)+2, i+2) for i in range(1, int(math.sqrt(number))+1) if number % i == 0 ]

        