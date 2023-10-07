N = int(input())

T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
# dp[i] = (i+1)일차부터 받을 수 있는 금액의 최댓값.
dp = [0]*(N+1)

for i in range(N):
    dp[i] = max(dp[i], dp[i-1])
    if i + T[i] > N:
        continue
    
    dp[i + T[i]] = max(dp[i] + P[i], dp[i + T[i]])

print(max(dp))