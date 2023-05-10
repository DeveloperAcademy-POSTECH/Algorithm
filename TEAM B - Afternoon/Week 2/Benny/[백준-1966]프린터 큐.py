'''
https://www.acmicpc.net/problem/1966
'''
from collections import deque

test_cases = int(input())
while test_cases > 0:
    num_of_docu, idx = map(int,(input().split()))
    impts = list(map(int, input().split()))
    dq = deque(impts)
    count = 0
    
    while dq:    
        while dq[0] != max(dq):
            dq.rotate(-1)
            if idx <= 0:
                idx += len(dq)
            idx -= 1
        
        if idx == 0:
            dq.popleft()
            count += 1
            break
        
        dq.popleft()
        idx -= 1
        count += 1
        
    print(count)
    test_cases -= 1
