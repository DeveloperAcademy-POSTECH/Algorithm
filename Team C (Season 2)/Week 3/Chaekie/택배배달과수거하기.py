def solution1(cap, n, deliveries, pickups):
    answer = 0
    total_sum = [0, 0]
    
    # deliveries, pickups의 마지막 값이 0일 경우 처리
    while True:
        if len(deliveries) > 0 and deliveries[-1] == 0:
            deliveries.pop()
        else:
            break
            
    while True:
        if len(pickups) > 0 and pickups[-1] == 0:
            pickups.pop()
        else:
            break
            
    while deliveries or pickups:
        answer += max(len(deliveries), len(pickups)) * 2
        
        for i in range(len(deliveries)-1, -1, -1):
            if total_sum[0] + deliveries[i] <= cap:
                total_sum[0] += deliveries[i]
                deliveries.pop()
            else:
                deliveries[i] -= cap - total_sum[0]
                break
                
        for i in range(len(pickups)-1, -1, -1):
            if total_sum[1] + pickups[i] <= cap:
                total_sum[1] += pickups[i]
                pickups.pop()
            else:
                pickups[i] -= cap - total_sum[1]
                break
    
        total_sum = [0, 0]
        
    return answer