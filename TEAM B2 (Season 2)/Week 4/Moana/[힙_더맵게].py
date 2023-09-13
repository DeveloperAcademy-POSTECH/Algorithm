import heapq

def solution(scoville, K):
    answer = 0
    food = 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            break
            
        if len(scoville) == 1:
            answer = -1
            break
            
        front = heapq.heappop(scoville)
        rear = heapq.heappop(scoville)
        
        food = front + (rear * 2)
        heapq.heappush(scoville, food)
        answer += 1
        
    return answer

