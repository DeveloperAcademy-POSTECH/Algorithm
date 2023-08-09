from collections import deque

tree = {}

def drop(q, counts, current):
    while current in tree.keys():
        idx, childs = tree[current]
        child = childs[idx]
        tree[current][0] = (tree[current][0] + 1) % len(childs)
        current = child
        
    counts[current - 1] += 1
    q.append(current - 1)
    
def check(target, counts):
    for idx in range(len(target)):
        if counts[idx] > target[idx]:
            return 'impossible'
        elif counts[idx] * 3 < target[idx]:
            return 'continue'
        
    return 'pass'

def solution(edges, target):
    answer = []
    q = deque()
    counts = [0 for _ in range(len(edges) + 1)]
    
    for parent, child in edges:
        if parent in tree.keys():
            tree[parent][1].append(child)
            tree[parent][1].sort()
        else:
            tree[parent] = [0, [child]]
    
    while True:
        drop(q, counts, 1)
        
        ch = check(target, counts)
        if ch == 'impossible':
            return [-1]
        elif ch == 'pass':
            break
        elif ch == 'continue':
            continue

    # print(target)
    # print(counts)
    # print(q)
    # print()
            
    while q:
        idx = q.popleft()
        # print(idx)
        counts[idx] -= 1

        if not counts[idx]:
            answer.append(target[idx])
            target[idx] = 0
        else:
            if target[idx] - 1 <= counts[idx] * 3: # 1을 떨어뜨려도 됨
                target[idx] -= 1
                answer.append(1)
            elif target[idx] - 2 <= counts[idx] * 3: # 2를 떨어뜨려도 됨
                target[idx] -= 2
                answer.append(2)
            else: # 3만 떨어뜨릴 수 있음
                target[idx] -= 3
                answer.append(3)

        # print(target)
        # print(counts)
        # print(answer)
        # print()

    return answer
