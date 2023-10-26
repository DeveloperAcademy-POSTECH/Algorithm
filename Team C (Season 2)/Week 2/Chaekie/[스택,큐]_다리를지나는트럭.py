from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    waiting_queue = deque(truck_weights)
    crossing_queue = deque()
    time_queue = deque()
    
    while waiting_queue:
        answer += 1
        if sum(crossing_queue) + waiting_queue[0] <= weight:
            item = waiting_queue.popleft()
            crossing_queue.append(item)
            time_queue.append(bridge_length)

        for i in range(len(time_queue)):
            time_queue[i] -= 1
        
        if time_queue[0] == 0:
            time_queue.popleft()
            crossing_queue.popleft()
            
    return answer + time_queue[-1]