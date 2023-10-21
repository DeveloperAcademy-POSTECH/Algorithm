N, L = map(int, input().split())

pool = []
for _ in range(N):
    pool.append(tuple(map(int, input().split())))
pool = sorted(pool)

# 맨 마지막 널빤지의 시작 좌표.
board = -(L+1)
res = 0

for s, e in pool:
    if board+L-1 < s:
        board = s
        res += 1
        
    while board+L < e:
        board = board+L
        res += 1

print(res)