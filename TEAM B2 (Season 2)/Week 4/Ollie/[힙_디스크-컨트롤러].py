
# 디스크 컨트롤러
# https://school.programmers.co.kr/learn/courses/30/lessons/42627
from typing import List
import heapq
import math

"""
# answer 1
음.. 다음 task 를 고를 때, 소요시간이 가장 적은 친구부터 고른다면 평균 소요 시간이 min이 될까? 일단 그렇게 생각하고 진행해보자.
"""

def solution1(jobs: List[List[int]]) -> int:
    hq = []
    for fromTime, cost in jobs:
        heapq.heappush(hq, (cost, fromTime))

    time = 0
    total = 0
    while hq:
        cost, fromTime = heapq.heappop(hq)
        time = time + cost if time > fromTime else fromTime + cost
        total += time - fromTime
    
    return math.floor(total / len(jobs))



"""
# answer 2
음.. 다음 task 를 고를 때, 소요시간이 가장 적은 친구부터 고른다면 평균 소요 시간이 min이 될까? 일단 그렇게 생각하고 진행해보자.

[[0, 3], [10, 1]] => 2
[[7, 8], [3, 5], [9, 6]] => 9
[[1, 4], [7, 9], [1000, 3]] => 5
[[0, 1], [2, 2], [2, 3]] => 2
"""

def solution(jobs: List[List[int]]) -> int:
    hq = []
    # pop - O(1)을 위해 jobs를 내림차순으로 정렬한다.
    jobs_rev = sorted(jobs, key=lambda x: (x[0], x[1]), reverse=True)
    # 최초의 job을 pop한다.
    fromTime, cost = jobs_rev.pop()
    heapq.heappush(hq, (cost, fromTime))

    # 변수 초기화
    time, total = 0, 0

    while hq:
        cost, fromTime = heapq.heappop(hq)
        time = time + cost if time > fromTime else fromTime + cost
        total += (time - fromTime)
        # 지난 시간보다 요청시간이 작은 job을 모두 hq에 push한다.
        while jobs_rev and jobs_rev[-1][0] < time:
            fromTime, cost = jobs_rev.pop()
            heapq.heappush(hq, (cost, fromTime))
        # time이 jobs_rev[-1][0]보다 작으면, 즉 지난 시간이 요청시간보다 작은 경우, 위의 while문은 동작하지 않음. 그래서 hq는 빈 상태일거임. 그때는 hq에서 1회 push한다.
        if not hq and jobs_rev:
            fromTime, cost = jobs_rev.pop()
            heapq.heappush(hq, (cost, fromTime))        
            
    # 소수점 이하는 버린다.
    return math.floor(total / len(jobs))


if __name__ == "__main__":
    # jobs = [[0, 1], [2, 2], [2, 3]]
    # sol = solution(jobs)
    # print(sol)
    print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
    
    print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
    print(solution([[100, 100], [1000, 1000]]), 500)

    # 통과----
    print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
    print(solution([[0, 3], [1, 9], [2, 6]]), 9)
    print(solution([[0, 1]]), 1)
    print(solution([[1000, 1000]]), 1000)
    print(solution([[0, 1], [0, 1], [0, 1]]), 2)
    print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
    print(solution([[0, 1], [1000, 1000]]), 500)
    
    print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
    