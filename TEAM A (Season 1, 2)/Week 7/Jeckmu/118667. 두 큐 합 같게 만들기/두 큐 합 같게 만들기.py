from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    # 홀수면 절반 불가
    total = sum(queue1)+sum(queue2)
    if total % 2 == 1:
        return -1
    
    S = sum(queue1)
    
    for i in range(len(queue1)*4):
        if S == total/2:
            return i
        elif S > total/2:
            a = queue1.popleft()
            queue2.append(a)
            S -= a
        else:
            a = queue2.popleft()
            queue1.append(a)
            S += a
    
    return -1