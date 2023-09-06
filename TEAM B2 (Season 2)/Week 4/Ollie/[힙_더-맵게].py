
# 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
from typing import List
import heapq

# 가장 작은 항목은 heap[0]이다.
# heap.sort()는 힙의 불변성을 유지한다!

def solution(scoville: List[int], K: int) -> int:
    # scoville을 heap화 한다.
    heapq.heapify(scoville)
    answer = 0
    
    # scoville의 최소값이 K 이상될 때 까지 아래 반복문을 실행한다.
    while scoville[0] < K:
        # 음식은 2개를 섞어야 하므로, 섞어야 하는데 scoville의 길이가 1개라면 실패
        if len(scoville) == 1: return -1
        
        # pop을 2회한 후 new_food를 계산, 이를 다시 scoville에 넣는다.
        min_food, next_min_food = heapq.heappop(scoville), heapq.heappop(scoville)
        new_food = min_food + (next_min_food * 2)
        heapq.heappush(scoville, new_food)
        answer += 1
    
    return answer