from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque([0] * bridge_length)
    truck = deque(truck_weights)
    sum_weight = 0
    while True :
        sum_weight -= (queue.popleft())
        if not truck :
            truck.append(0)
        if sum_weight + truck[0] <= weight :
            sum_weight += truck[0]
            queue.append(truck.popleft())
            answer += 1
        else : 
            queue.append(0)
            answer += 1
        if sum_weight == 0 :
            return answer