# 1647번: 도시 분할 계획

import sys
import heapq

input = sys.stdin.readline

# N <= 10^5, M <= 10^6
N, M = map(int, input().rstrip().split())

# 1. 그래프를 두 개의 서브그래프로 나누면서
# 2. 모든 노드끼리의 경로가 최솟값이 되도록 해야 한다.

# 다익스트라? 이분 그래프? Disjoint Set? MST?
# MST를 구성한 다음, 가장 비용이 큰 간선 하나를 제외한다면?

mst = []
edges = []
groups = [i for i in range(N + 1)] # 부모를 자기 자신으로 초기화

for _ in range(M):
    A, B, C = map(int, input().rstrip().split())

    heapq.heappush(edges, (C, A, B))

def find(current):
    if groups[current] != current:
        groups[current] = find(groups[current])
        
    return groups[current]

def union(A, B):
    group_A = find(A)
    group_B = find(B)

    if group_A < group_B:
        groups[group_B] = A
    else:
        groups[group_A] = B

mst = []

while len(mst) < N - 1:
    C, A, B = heapq.heappop(edges)

    if find(A) != find(B):
        union(A, B)
        mst.append(C)

        # print(groups)
        # print(A, B)

print(sum(mst) - max(mst))
