import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K:
        if len(scoville) == 1:
            return -1
        s1, s2 = heapq.heappop(scoville), heapq.heappop(scoville)
        new = s1 + s2*2
        heapq.heappush(scoville, new)
        answer += 1
    return answer