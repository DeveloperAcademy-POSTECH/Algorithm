from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque()
    count = 1

    for i, progress in enumerate(progresses):
        queue.append(math.ceil((100 - progress) / speeds[i]))
    print(queue)
    
    while queue:
        for i in range(1, len(queue)):
            if queue[i] <= queue[0]:
                count += 1
            else:
                break
        for i in range(count):
            queue.popleft()
        answer.append(count)
        count = 1
    
    return answer