# N <= 100, N^3 해도 100만이니까 여유롭다
# RGB 구역을 나누고
# 나눠진 구역이 일반인과 적록색약의 기준에서 총 몇개인지를 출력하면 됨


# 2
# RG
# GR
# 같은 경우, 색약의 경우 저 네칸이 다 하나로 보이기 때문에 결과값이 4, 1 이 나와야함

import sys
sys.stdin = open("10026_RedGreenColorBlindness/RedGreenColorBlindness.txt", "r")

N = int(sys.stdin.readline())

matrix = []
visited = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    matrix.append(list(sys.stdin.readline().rstrip()))

stack = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]





def dfs(r, c):
    stack = [[r,c]]
    while stack:
        r, c = stack.pop()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if not(0<=nr<N and 0<=nc<N):
                continue
            
            if visited[nr][nc]:
                continue

            if matrix[nr][nc] == color:
                stack.append([nr, nc])
                visited[nr][nc] = 1
    

# 정상인
R = 0
G = 0
B = 0

for i in range(N): # 배열을 돌면서 방문하지 않은 지점을 찾음
    for j in range(N):
        if not visited[i][j]:
            stack.append([i, j]) # 이 지점부터 dfs 시작
            visited[i][j] = 1

            color = matrix[i][j]

            if color == "R":
                R += 1
            elif color == "G":
                G += 1
            else:
                B += 1

            dfs(i, j)

normalColor = R+G+B

# 적록 색약
R = 0
G = 0
B = 0

for i in range(N): #적록색약 용 matrix
    for j in range(N):
        if matrix[i][j] == "G":
            matrix[i][j] = "R"
        visited[i][j] = 0

for i in range(N): # 배열을 돌면서 방문하지 않은 지점을 찾음
    for j in range(N):
        if not visited[i][j]:
            stack.append([i, j]) # 이 지점부터 dfs 시작
            visited[i][j] = 1

            color = matrix[i][j]

            if color == "R":
                R += 1
            elif color == "G":
                G += 1
            else:
                B += 1

            dfs(i, j)

colorBlindnessColor = R+G+B

print(f"{normalColor} {colorBlindnessColor}")