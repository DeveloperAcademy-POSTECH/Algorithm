# https://www.acmicpc.net/submit/1890/68688960

import sys

input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
    
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

dr, dc = [0, 1], [1, 0]

for r in range(n):
    for c in range(n):
        for i in range(2):
            nr, nc = r + dr[i] * board[r][c], c + dc[i] * board[r][c]
            if 0 <= nr < n and 0 <= nc < n:
                dp[nr][nc] += dp[r][c]

print(dp[-1][-1] // 4)