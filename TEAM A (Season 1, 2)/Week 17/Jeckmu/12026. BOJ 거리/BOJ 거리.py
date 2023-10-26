N = int(input())
s = list(input())
INF = 10e9
dp = [INF]*N

dp[N-1] = 0
for i in range(N-1, -1, -1):
    for j in range(i-1, -1, -1):
        if s[i] == "B":
            if s[j] == "J":
                dp[j] = min(dp[j], dp[i] + (i-j)**2)
        elif s[i] == "O":
            if s[j] == "B":
                dp[j] = min(dp[j], dp[i] + (i-j)**2)
        elif s[i] == "J":
            if s[j] == "O":
                dp[j] = min(dp[j], dp[i] + (i-j)**2)
                
if dp[0] == INF:
    print(-1)
else:
    print(dp[0])