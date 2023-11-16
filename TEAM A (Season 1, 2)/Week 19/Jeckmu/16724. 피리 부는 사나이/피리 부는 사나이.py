N, M = map(int, input().split())

g = []
for _ in range(N):
    g.append(list(input()))
    
# 좌표가 [r][c]일 때, 임의로 칸의 번호를 `r * M + c` 로 지정.
root = {i: i for i in range(N*M)}

def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx < ry:
        root[ry] = rx
    else:
        root[rx] = ry

def go(r, c):
    nowIndex = r*M+c
    if g[r][c] == "R":
        if c == M-1:
            return
        union(nowIndex, nowIndex+1)
    elif g[r][c] == "L":
        if c == 0:
            return
        union(nowIndex, nowIndex-1)
    elif g[r][c] == "U":
        if r == 0:
            return
        union(nowIndex, nowIndex-M)
    elif g[r][c] == "D":
        if r == N-1:
            return
        union(nowIndex, nowIndex+M)

for r in range(N):
    for c in range(M):
        go(r, c)

result = {}
for r in range(N):
    for c in range(M):
        nowIndex = r*M+c
        result[find(nowIndex)] = 1

print(len(result))