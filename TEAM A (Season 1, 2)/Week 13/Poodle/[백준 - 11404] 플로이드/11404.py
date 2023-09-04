# 백준 11404번: 플로이드 (2회차)

import sys

input = sys.stdin.readline

# N <= 10^2
N = int(input())

# M <= 10^5
M = int(input())

# O(N^3) -> 10^6 -> 플로이드-워셜

costs = [[int(1e9) for _ in range(N)] for _ in range(N)]

for i in range(N):
    costs[i][i] = 0

for _ in range(M):
    A, B, cost = map(int, input().rstrip().split())

    costs[A - 1][B - 1] = min(costs[A - 1][B - 1], cost)
    # costs[B - 1][A - 1] = min(costs[B - 1][A - 1], cost)

for k in range(N):
    for i in range(N):
        for j in range(N):
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

for i in range(N):
    for j in range(N):
        if costs[i][j] == int(1e9):
            costs[i][j] = 0

for row in costs:
    print(*row)
