N = int(input())

mat = []

for _ in range(N):
    r, c = map(int, input().split())
    mat.append((r, c))

# NxM 행렬과 MxK 행렬을 곱하면, NxMxK.
# dp[i][j]는 i+1번째 행렬부터, j+1번째 행렬까지 곱했을 때의 곱셈 연산 횟수의 minimum.

# k = i ~ j-1 사이의 임의의 값일 때,
# dp[i][j] = dp[i][k] + dp[k+1][j] + mat[i][0]*mat[k][1]*mat[j][1] 의 값들 중 최소값.
dp = [[0]*N for _ in range(N)]

for i in range(N-1):
    dp[i][i+1] = mat[i][0]*mat[i+1][0]*mat[i+1][1]

for L in range(2, N):
    i = 0
    j = L

    while j < N:
        dp[i][j] = 2**31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] +
                           mat[i][0]*mat[k][1]*mat[j][1])
        i += 1
        j += 1

print(dp[0][N-1])