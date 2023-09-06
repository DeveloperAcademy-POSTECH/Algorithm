# https://school.programmers.co.kr/learn/courses/30/lessons/86971

def solution(n, wires):
    # 2트
    # Union Find를 공부해서 적용해보자 - getK
    
    answer = 100 # |2k-n|은 100보다 같거나 클 수 없다.
    
    def getK(wires):
        parents = list(range(n+1))
        
        def getParentOf(node):
            if parents[node] == node: return node
            return getParentOf(parents[node])
        
        def unionParent(nodeA, nodeB):
            nodeA, nodeB = getParentOf(nodeA), getParentOf(nodeB)
            if nodeA > nodeB: parents[nodeA] = nodeB
            else: parents[nodeB] = nodeA
        
        def hasSameParents(nodeA, nodeB):
            return getParentOf(nodeA) == getParentOf(nodeB)
        
        def getConnectedNumberOf(nodeA):
            return len([node for node in parents if getParentOf(nodeA) == getParentOf(node)])
        
        
        for arr, dest in wires:
            unionParent(arr, dest)
        return getConnectedNumberOf(1)
    
                

    for i in range(len(wires)):
        k = getK(wires[:i] + wires[i+1:])
        answer = min(answer, abs(2*k-n))
        if answer == 0:
            return 0
    
    return answer
    

def solution(n, wires):
    # 1트의 반례는 아래와 같음
    # n =6, wires = [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]], answer = 2
    
    # wire를 한 개를 빼요
    # 그랬을 때 모두 연결된 것을 k개라고 하면, |2k - n|가 정답!
    # 얘가 min 값이 되도록 송전탑을 자르면 됩니다. 모두를 구한 후 min값을 출력하자.
    # 만약 0이 있으면 빨리 탈출
    # 틀린 이유.. 
    
    if n == 2:
        return 0
    
    answer = 100 # |2k-n|은 100보다 같거나 클 수 없다.
    
    def getK(wires):
        wireSet = set(wires[0])
        for arr, dest in wires[1:]:
            if arr in wireSet or dest in wireSet:
                wireSet.update([arr, dest])
        print(len(wireSet), wires)
        return len(wireSet)
            
    for i in range(len(wires)):
        k = getK(wires[:i] + wires[i+1:])
        answer = min(answer, abs(2*k-n))
        if answer == 0:
            return 0
    
    return answer