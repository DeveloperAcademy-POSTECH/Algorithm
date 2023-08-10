def solution(cap, n, deliveries, pickups):
    deliverPointer = n-1
    pickupPointer = n-1
    answer = 0

    while pickups[pickupPointer] != 0 or deliveries[deliverPointer] != 0:
        length = []
        # 제일 먼 집부터 배달을 처리해나감
        temp = 0
        for i in range(deliverPointer, -1, -1):
            if cap >= temp + deliveries[i]:
                temp += deliveries[i]
                deliveries[i] = 0
                deliverPointer -= 1
                length.append(i)
            else:
                # cap < temp + deliveries[i]
                deliveries[i] -= cap-temp
                temp = cap
                length.append(i)
                break

        # 그리고 갔다 오면서 수거도
        temp = 0
        for i in range(pickupPointer, -1, -1):
            if cap >= temp + pickups[i]:
                temp += pickups[i]
                pickups[i] = 0
                pickupPointer -= 1
                length.append(i)
            else:
                # cap < temp + pickups[i]
                pickups[i] -= cap-temp
                temp = cap
                length.append(i)
                break

        if length:
            answer += (max(length)+1)*2
            
    return answer