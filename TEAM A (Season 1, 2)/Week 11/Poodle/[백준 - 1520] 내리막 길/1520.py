# 백준 1520번: 내리막 길

import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# M, N <= 5 * 10^2
M, N = map(int, input().rstrip().split())

maps = [list(map(int, input().rstrip().split())) for _ in range(M)]
# for row in maps:
#     print(row)
# print()

next_moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

# dp[r][c] = (r, c)에서 도착점까지 도달하는 방법의 경우의 수
dp = [[-1 for _ in range(N)] for _ in range(M)]

def dfs(r, c):
    if r == M - 1 and c == N - 1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]
    
    ways = 0
    for dr, dc in next_moves:
        if 0 <= r + dr < M and 0 <= c + dc < N:
            if maps[r][c] > maps[r + dr][c + dc]:
                ways += dfs(r + dr, c + dc)

    dp[r][c] = ways
    return dp[r][c]
    
dfs(0, 0)
# for row in dp:
#     print(row)
print(dp[0][0])
