import sys
input = sys.stdin.readline
targetlist = list(map(int,input().split(" ")))
targetnum = len(targetlist)

INF = 1e8
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(targetnum)]
def move(x,y):
    if(x == 0):
        return 2
    elif x==y:
        return 1
    elif abs(x-y)==2 :
        return 4
    else:
        return 3
dp[0][0][0] = 0
for i in range(targetnum-1):
    target = targetlist[i]
    for l in range(5):
        for r in range(5):
            dp[i+1][l][target] = min(dp[i][l][r]+move(r,target), dp[i+1][l][target]) # 오른발 움직이는 경우
            dp[i+1][target][r] = min(dp[i][l][r]+move(l,target), dp[i+1][target][r]) # 왼발
result = INF
for i in range(5):
    for j in range(5):
        result = min(result,dp[len(targetlist)-1][i][j])
print(result)