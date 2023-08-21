# 백준 11049번: 행렬 곱셈 순서

import sys

input = sys.stdin.readline

# N <= 5 * 10^2
N = int(input())

# (5 * 3 * 2) + (5 * 2 * 6) or
# (3 * 2 * 6) + (5 * 3 * 6)

# 5 3 2 6
# 5

r, c = map(int, input().rstrip().split())
arr = [r, c]

for _ in range(N - 1):
    _, c = map(int, input().rstrip().split())
    arr.append(c)

# dp[i][j] = i번째부터 j번째 행렬까지의 최소 곱셈 횟수
dp = [[0 for _ in range(N)] for _ in range(N)]
# for row in dp:
#     print(row)
# print()

# N = 3
for d in range(N): # 0 1 2
    for i in range(N - d): # (0 1 2) (0 1) (0)
        j = i + d # (0 1 2) (1 2) (2)

        if i == j:
            continue

        dp[i][j] = int(1e9)
        for k in range(i, j):
            dp[i][j] = min(dp[i][j],\
                           (dp[i][k] + dp[k + 1][j]) + (arr[i] * arr[k + 1] * arr[j + 1]))

    # for row in dp:
    #     print(row)
    # print()

print(dp[0][-1])
