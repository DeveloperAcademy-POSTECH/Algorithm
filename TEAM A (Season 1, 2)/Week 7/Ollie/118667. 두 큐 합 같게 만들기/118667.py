# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3
# 두 큐 합 같게 만들기

from collections import deque



def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)

    if (sum1 + sum2) & 1 == 1:
        return -1

    # maximumCount = len(q1) * 2
    maximumCount = len(q1) * 3
    count = 0

    while count < maximumCount:
        if sum1 == sum2:
            return count
        elif sum1 > sum2:
            curNum = q1.popleft()
            q2.append(curNum)
            sum1, sum2 = sum1 - curNum, sum2 + curNum
        else:
            curNum = q2.popleft()
            q1.append(curNum)
            sum1, sum2 = sum1 + curNum, sum2 - curNum
        count += 1
    return -1

