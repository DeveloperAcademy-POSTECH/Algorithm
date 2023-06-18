# 백준 2342번: Dance Dance Revolution

import sys

input = sys.stdin.readline

directions = list(map(int, input().rstrip().split()))
N = len(directions) - 1
directions.insert(0, 0)

power = {
    0: {
        1: 2,
        2: 2,
        3: 2,
        4: 2
    },
    1: {
        1: 1,
        2: 3,
        3: 4,
        4: 3
    },
    2: {
        1: 3,
        2: 1,
        3: 3,
        4: 4
    },
    3: {
        1: 4,
        2: 3,
        3: 1,
        4: 3
    },
    4: {
        1: 3,
        2: 4,
        3: 3,
        4: 1
    }
}

left, right = 0, 0
answer = 0

# dp[n][l][r] = n번째 발판까지 밟으면서 왼쪽 발이 l, 오른쪽 발이 r에 있을 때 드는 힘
dp = [[[400001 for _ in range(5)] for _ in range(5)] for _ in range(N + 1)]

# 시작점 설정
dp[0][0][0] = 0

# 명령의 개수 <= 10^5
for i in range(1, N + 1):
    # 이번에 밟아야 하는 발판
    current = directions[i]
    # print(current)

    # 이번 i번째 발판을 밟는 데 걸리는 힘을 계산
    # 1. 왼쪽 발을 움직이는 경우
    for j in range(5): # 오른쪽 발의 이전 위치
        for k in range(5): # 왼쪽 발의 이전 위치 (움직일 예정)
            dp[i][current][j] = min(dp[i][current][j], dp[i - 1][k][j] + power[k][current])
    # 2. 오른쪽 발을 움직이는 경우
    for j in range(5): # 왼쪽 발의 이전 위치
        for k in range(5): # 오른쪽 발의 이전 위치 (움직일 예정)
            dp[i][j][current] = min(dp[i][j][current], dp[i - 1][j][k] + power[k][current])
    
    # for row in dp[i]:
    #     print(row)
    # print()

answer = 400001
for i in range(5):
    for j in range(5):
        answer = min(answer, dp[N][i][j])

print(answer)
