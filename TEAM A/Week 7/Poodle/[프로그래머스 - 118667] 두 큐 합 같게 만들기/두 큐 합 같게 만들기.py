from collections import deque

def solution(queue1, queue2):
    answer = 600001
    
    total_sums = sum(queue1) + sum(queue2)
    if total_sums % 2 != 0: return -1
    target = total_sums // 2
    
    q = queue1 + queue2
    N = len(q)
    M = len(queue1)

    left, right = 0, M - 1
    temp = sum(q[left : right + 1])
    cnt = 0
    
    while True:
        # print(cnt, " : ", left, right, temp)
        if temp < target:
            if right >= N - 1:
                break
            right += 1
            temp += q[right]
            cnt += 1
        else:
            if temp == target:
                # print(f"found! -> {left}, {right}")
                answer = min(answer, cnt)
            temp -= q[left]
            left += 1
            cnt += 1
    
    return answer if answer != 600001 else -1
