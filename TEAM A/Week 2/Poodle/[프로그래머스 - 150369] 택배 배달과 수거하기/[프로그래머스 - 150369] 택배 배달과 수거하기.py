def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # cap: 트럭에 실을 수 있는 택배 상자의 최대 개수
    # n: 집의 개수
    
    # N(<= 10^5)개의 집에 택배 배달을 하려고 함
    # 택배는 택배 + 택배 상자로 구성되어 있으며, 택배 상자는 수거해야 함
    # i번째 집은 물류창고에서 i만큼 떨어져 있음
    
    # 그리디 문제 같은데...
    
    from collections import deque
    
    deli_stack = deque([(i + 1, deliveries[i]) for i in range(n)])
    pick_stack = deque([(i + 1, pickups[i]) for i in range(n)])
    
    while deli_stack or pick_stack:
        while deli_stack and deli_stack[-1][1] == 0:
            deli_stack.pop()
        while pick_stack and pick_stack[-1][1] == 0:
            pick_stack.pop()
            
        deli_cap = cap
        pick_cap = cap
        max_distance = 0
            
        while deli_stack and deli_cap:
            distance, boxes = deli_stack.pop()
            max_distance = max(max_distance, distance)
            
            if boxes > deli_cap:
                deli_stack.append((distance, boxes - deli_cap))
                break
            else:
                deli_cap -= boxes
                
        while pick_stack and pick_cap:
            distance, boxes = pick_stack.pop()
            max_distance = max(max_distance, distance)
            
            if boxes > pick_cap:
                pick_stack.append((distance, boxes - pick_cap))
                break
            else:
                pick_cap -= boxes
        
        answer += (max_distance * 2)
        
        # print(deli_stack)
        # print(pick_stack)
        # print()
            
    return answer