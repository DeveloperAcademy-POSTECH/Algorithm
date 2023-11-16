from collections import deque

# input
N = int(input())
M = int(input())
root = {i: i for i in range(1, N+1)}
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

# Union-Find
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
        
# MST
edges = sorted(edges)
result = 0
for cost, a, b in edges:
    if find(a) == find(b):
        continue
    
    union(a, b)
    result += cost
    
print(result)