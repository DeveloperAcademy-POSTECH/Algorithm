from collections import deque
n, m = map(int, input().split())

root = {i: i for i in range(n)}

def find(x):
    if root[x] == x:
        return x
    else:
        # 경로 압축
        root[x] = find(root[x])
        return root[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        root[x] = y
    else :
        root[y] = x

for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i+1)
        break
    union(a, b)
else:
    print(0)