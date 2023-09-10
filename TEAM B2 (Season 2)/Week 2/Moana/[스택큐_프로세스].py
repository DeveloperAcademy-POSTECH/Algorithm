from collections import deque

def solution(priorities, location):
    answer = 1
    ind = [0 for _ in range(len(priorities))]
    ind[location] = 1
    index = deque(ind)
    priority = deque(priorities)
    
    while True:
        tmp = max(priority)
        if priority[0] != tmp:
            priority.append(priority.popleft())
            index.append(index.popleft())
        elif priority[0] == tmp:
            if index[0] == 1:
                break
            else:
                priority.popleft()
                index.popleft()
                answer += 1

    return answer

