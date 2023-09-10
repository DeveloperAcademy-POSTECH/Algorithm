# 11049 행렬 곱셈 순서
# https://www.acmicpc.net/problem/11049


# 추가문제
# 11066 파일 합치기
# https://www.acmicpc.net/problem/11066

# 1초
# 크기가 N x M 인 행렬 A
# 크기가 M x K 인 행렬 B
# 필요한 곱셈 연산의 수는 총 N x M x K 번

# 행령 N 개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산의 최솟값은?

# 행렬 연산의 숫자가 바뀌면 안됨

# (연쇄행렬) 최소 곱셈 알고리즘
# 행렬 A,B,C,D 4개가 존재한다.
# 각각 행렬의 차수는 20x1, 1x30, 30x10, 10x10이라고 한다.
# 4개의 행렬은 여러가지 방법으로 곱할 수 있지만,
# 다음 4개의 경우에 대하여 생각해볼때, 곱셈 횟수를 비교하면 아래와 같다.

# ((A*B)*C)*D) = (20*1*30) + (20*30*10) + (20*10*10) = 8,600
# A*(B*(C*D)) = (30*10*10) + (1*30*10) + (20*1*10) = 3,500
# (A*B)*(C*D) = (20*1*30) + (30*10*10) + (20*30*10) = 9,600
# (A*((B*C)*D) = (1*30*10) + (1*10*10) + (20*1*10) = 600

# https://rccode.tistory.com/155

# dp[i][j]는 i번째 행렬 ~ j번째 행렬까지의 최소곱을 뜻한다.

# 대각선 연산을 해줘야하는 이유
# dp[0][3] 을 구하려고 할 때를 생각해보자. 이 경우를 나눠본다면
# 1. dp[0][0] + dp[1][3]
# 2. dp[0][1] + dp[2][3]
# 3. dp[0][2] + dp[3][3]
# 이 있겠다.
# 이 중에서 최소의 값을 선택하면 된다.
# 그렇기 때문에 모든 칸의 값들을 구하면서 진행하는것 -> 맞나??

import sys
sys.stdin = open("11049_matrixMultiplication/matrixMultiplication.txt", "r")
input = sys.stdin.readline

N = int(input())

info = []
for _ in range(N-1):
    info.append(list(map(int, input().split())))


dp = [[0] * N for _ in range(N)]

for d in range(N):
    for i in range(N-d):
        j = i + d

        if i == j:
            continue

        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + info[i][0]*info)

print(dp[0][-1])



# import sys
# sys.stdin = open("11049_matrixMultiplication/matrixMultiplication.txt", "r")
# input = sys.stdin

# N = int(input.readline())

# info = []
# numSet = []
# for _ in range(N):
#     r, c = list(map(int, input.readline().split()))
#     info.append([r, c])

# for i in range(len(info)-1):
#     numSet.append(info[i][1])

# priorityList = sorted(list(numSet))

# def calculate(arr):
#     n, m = arr[0]
#     answer = 0
#     for i in range(1, len(arr)):
#         a, b = arr[i]
#         temp = (n * m * b)
#         answer += temp
#         m = b
    
#     newCenter = [[n, m]]

#     return (newCenter, answer)

# result = 0

# while priorityList:
#     currentNumber = priorityList.pop()
#     print(info)
#     print(result)
#     for i in range(len(info)):
#         if (info[i][1] == currentNumber):
#             left = info[:i]
#             arr = info[i:i+2]
#             right = info[i+2:]
#             returnValue = calculate(arr)
#             result += returnValue[1]
#             info = left + returnValue[0] + right
#             break

# print(result)