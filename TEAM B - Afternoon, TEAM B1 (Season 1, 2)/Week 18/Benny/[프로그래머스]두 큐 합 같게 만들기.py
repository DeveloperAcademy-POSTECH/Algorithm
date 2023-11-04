# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 두 큐 합 같게 만들기

from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    
    total_len = len(queue1) + len(queue2)
    total = sum_q1 + sum_q2
    
    if total % 2 != 0:
        return -1
    ideal = total // 2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    while sum_q1 != ideal and answer < total_len * 2:
        if sum_q1 > ideal:
            element = queue1.popleft()
            queue2.append(element)
            answer += 1
            sum_q1 -= element
            sum_q2 += element
        else:
            element = queue2.popleft()
            queue1.append(element)
            answer += 1
            sum_q1 += element
            sum_q2 -= element
            
    return answer if sum_q1 == ideal else -1