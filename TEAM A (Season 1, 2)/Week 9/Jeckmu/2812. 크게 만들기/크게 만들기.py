from collections import deque

N, K = map(int, input().split())
num = deque(list(input()))
res = deque()

for _ in range(N):
    a = num.popleft()
    while len(res) > 0 and K > 0 and res[len(res)-1] < a:
        res.pop()
        K -= 1

    res.append(a)

if K != 0:
    while K > 0:
        res.pop()
        K -= 1

print(*res, sep="")