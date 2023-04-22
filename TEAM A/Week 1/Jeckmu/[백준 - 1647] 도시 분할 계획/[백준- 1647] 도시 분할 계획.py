from collections import deque
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges = sorted(edges, key=lambda x: x[2])

dic = {i: i for i in range(1, N+1)}
result = []  # save costs for edges(result)


def find(x):  # Find(Union-Find), with optimization
    if dic[x] == x:
        return x
    dic[x] = find(dic[x])
    return dic[x]


def union(x, y):  # Union(Union-Find), connect to smaller one.
    rx = find(x)
    ry = find(y)
    if rx < ry:
        dic[ry] = rx
    else:
        dic[rx] = ry


for edge in edges:
    if len(result) == N-1:
        break

    a, b, c = edge
    # cycle 생성이 되지 않는다면,
    if find(a) != find(b):
        union(a, b)
        result.append(c)

print(sum(result) - max(result))
