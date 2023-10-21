T = int(input())

MOD = 1234567
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 순서
# dp[i][j] => 비밀번호 길이가 i일 때, j에서부터 출발하여 만들 수 있는 비밀번호의 개수.
dp = [[0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
out = {
    0: [7],
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8, 0],
    8: [5, 7, 9],
    9: [6, 8],
}

for i in range(2, 1001):
    tempList = []
    # dp[i][j] = dp[i-1][(인접한 숫자)] 들의 합
    # ex) dp[3][2] = dp[2][1] + dp[2][3] + dp[2][5]
    for s in range(10):
        tempSum = 0
        for e in out[s]:
            tempSum += dp[i-1][e]
        tempList.append(tempSum % MOD)
    dp.append(tempList)
    
for _ in range(T):
    print(sum(dp[int(input())]) % MOD)