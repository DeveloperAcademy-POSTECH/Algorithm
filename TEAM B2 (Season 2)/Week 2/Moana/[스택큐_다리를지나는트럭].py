from collections import deque

def solution(bridge_length, weight, truck_weights):
    tmp = [0] * bridge_length
    truck = deque(tmp)
    answer = 0 
    total = 0
    
    while truck_weights:
        total -= truck[0]
        truck.popleft()
        answer += 1
        
        if total + truck_weights[0] > weight:
            truck.append(0)
            
        else:
            total += truck_weights[0]
            truck.append(truck_weights.pop(0))

    return answer + bridge_length