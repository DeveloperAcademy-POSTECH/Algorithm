
# 기능 개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
from typing import List

def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    if not progresses: return []
    workingDayStack = workingDayList(progresses, speeds)[::-1]
    result: List[int] = []
    tempWorkingDay = workingDayStack.pop()
    tempCount = 1
    while workingDayStack:
        currentWorkingDay = workingDayStack.pop()
        if tempWorkingDay < currentWorkingDay:
            result.append(tempCount)
            tempWorkingDay = currentWorkingDay
            tempCount = 1
        else:
            tempCount += 1
    result.append(tempCount)
    return result

import math
def workingDayList(progresses: List[int], speeds: List[int]) -> List[int]:
    return [ math.ceil((100-progress)/speed) for (progress, speed) in zip(progresses, speeds)]
    

def solution(progresses, speeds):
    import math
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    
    answer = []
    cnt, curr_max = 1, days[0]
    for day in days[1:]:
        if curr_max < day:
            answer.append(cnt)
            cnt = 1
            curr_max = day
        else:
            cnt += 1
    answer.append(cnt)
    return answer