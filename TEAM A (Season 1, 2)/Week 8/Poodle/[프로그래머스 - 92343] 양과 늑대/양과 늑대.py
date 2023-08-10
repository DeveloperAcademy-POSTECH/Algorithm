from collections import defaultdict

childs = defaultdict(list)
max_sheeps = 1

def solution(info, edges):
    for parent, child in edges:
        childs[parent].append(child)
    
    def dfs(current, sheeps, wolfs, nexts):
        global max_sheeps
        
        # 현재 도착한 노드 번호를 제거
        nexts.remove(current)
        # 다음 갈 수 있는 노드 번호들을 추가
        for child in childs[current]:
            nexts.append(child)
        
        # 양에 도착한 경우
        if info[current] == 0: sheeps += 1
        # 늑대에 도착한 경우
        else: wolfs += 1
        
        # print(current, sheeps, wolfs, nexts)
        
        if sheeps <= wolfs: return
        if max_sheeps < sheeps:
            max_sheeps = sheeps
        
        for next_node in nexts:
            new_nexts = nexts.copy()
            dfs(next_node, sheeps, wolfs, new_nexts)
        
    visited = [False for _ in range(len(info))]
    dfs(0, 0, 0, [0])
    
    return max_sheeps
