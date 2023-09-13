from collections import deque
import copy

def bfs(n, info):
    result = []
    q = deque([([0] * 11, 0, n)])
    max_gap = 0
    
    while q:
        lion_info, cur_idx, arrows = q.popleft()
        if arrows == 0:
            apeach, lion = 0, 0
            for i in range(len(info)):
                if info[i] < lion_info[i]:
                    lion += 10 - i
                elif info[i] > 0:
                    apeach += 10 - i
                    
            if lion > apeach:
                gap = lion - apeach
                if max_gap < gap:
                    result = [lion_info]
                    max_gap = gap
                elif max_gap == gap:
                    result.append(lion_info)
                    
        elif cur_idx == 10:
            lion_info[cur_idx] = arrows
            arrows = 0
            apeach, lion = 0, 0
            for i in range(len(info)):
                if info[i] < lion_info[i]:
                    lion += 10 - i
                elif info[i] > 0:
                    apeach += 10 - i
            
            if lion > apeach:
                gap = lion - apeach
                if max_gap < gap:
                    result = [lion_info]
                    max_gap = gap
                elif max_gap == gap:
                    result.append(lion_info)
        
        else:
            temp = copy.deepcopy(lion_info)
            if info[cur_idx] + 1 <= arrows:
                temp[cur_idx] = info[cur_idx] + 1
                q.append((temp, cur_idx+1, arrows-temp[cur_idx]))
            
            temp = copy.deepcopy(lion_info)
            q.append((temp, cur_idx+1, arrows))
    
    return [-1] if result == [] else result[-1]

def solution(n, info):
    return bfs(n, info)
