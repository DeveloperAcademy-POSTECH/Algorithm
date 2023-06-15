# 모든 트럭이 다리를 건너려면 최소 몇초?
# 트럭은 최대 bridge_length 만큼 올라갈 수 있음
# 다르는 weight '이하' 까지의 무게를 견딜 수 있음
# 모든 트럭이 건너려면 최소 몇초가 걸리는지 return

# bridge_length 는 10,000 이하
# weight 는 10,000 이하
# truck_weight 는 10,000 이하 -> n^2 까지는 괜찮으려나? 아니면 그것보다 살짝 적게

# deque 를 사용해서 하나씩 뽑아내는게 나으려나?
# 무게 꽉 찼거나 못 올라오는 상황이면 0을 넣어서 길이와 시간을 맞추는식?
# -> 시간초과 남. 아마 truck 도 10,000 개 다리 길이도 10,000 면 시간초과나는듯 -> 다른 사람 풀이를 보니까 트럭 들어갈때랑 나갈때 각각 트럭의 무게에 대한 처리를 해주면 시간 안에 가능한듯 다시 해보자
# 그렇다면 그냥 array 에 담아서 각각마다 시간을 재고, 시간이 0이 되면 빼주는 식으로 해야할듯


from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    
    sum_weight = 0
    
    time = 0
    while sum_weight > 0 or len(trucks) > 0:
        sum_weight -= bridge.popleft()
        
        if len(trucks) > 0:
            if sum_weight + trucks[0] <= weight:
                sum_weight += trucks[0]
                bridge.append(trucks.popleft())
            else:
                bridge.append(0)
        else:
            bridge.append(0)
            
        time += 1

    return time
        
    
# def solution(bridge_length, weight, truck_weights):
#     bridge = deque()
#     trucks = deque(truck_weights)
    
#     time = 0
#     while len(bridge) > 0 or len(trucks) > 0: # 브릿지와 트럭 대기줄에 아무것도 없을때까지 진행
        
#         for i in range(len(bridge)):
#             bridge[i][1] -= 1 # 각각은 시간이 하나 지난만큼 뺴주고
            
#         # 우선은 내보낼 트럭을 빼는 작업
#         while len(bridge) > 0:
#             if bridge[0][1] <= 0: # 시간이 다 지났으면 popleft 로 앞에서부터 뺌
#                 bridge.popleft()
#             else:
#                 break # 시간이 다 지나지 않은 트럭이 있을경우 pop 을 멈춤
        
#         # 다리 총 무게 측정
#         weight_sum = 0
#         for i in range(len(bridge)):
#             weight_sum += bridge[i][0] # 총 무게 연산은 해주고

            
#         # 이제 넣을 수 있는 트럭 넣기
#         if len(trucks) > 0:
#             if weight_sum + trucks[0] <= weight:
#                 bridge.append([trucks.popleft(), bridge_length])
        
#         time += 1
        
#     return time


# from collections import deque

# def solution(bridge_length, weight, truck_weights):
    
#     bridge = deque([0 for _ in range(bridge_length)]) # 다리 길이 맞추기
#     trucks = deque(truck_weights) # truck 도 앞에서부터 빠지니까 deque 로 만듬
    
#     time = 0 # 걸리는 시간 count

    
#     while sum(bridge) != 0 or len(trucks) != 0:
#         bridge.popleft()
#         if len(trucks) > 0: # 남은 트럭이 있는 경우 -> 남은 트럭을 다리위에 올릴 수 있으면 올리기
#             if sum(bridge) + trucks[0] <= weight:
#                 bridge.append(trucks.popleft())
#             else:
#                 bridge.append(0)
#         else: # 남은 트럭이 없는 경우 -> 다리 위에 있는 트럭들만 나오면 끝
#             bridge.append(0)
            
#         time += 1
        
        
#     return time