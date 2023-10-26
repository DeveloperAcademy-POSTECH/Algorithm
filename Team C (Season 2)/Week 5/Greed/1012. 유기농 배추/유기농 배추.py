import sys
sys.setrecursionlimit(10**6) #재귀 최대 깊이를 설정해주어야함

# 서로 상하 좌우로 연결되어 있는 경우만 1마리의 배추흰지렁이 필요
def dfs(cur_y,cur_x):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        next_x, next_y = cur_x + dx[i], cur_y + dy[i]
        if next_x in range(row) and next_y in range(col) and graph[next_y][next_x] == 1:
            # 지나간 것들은 따로 -1로 표시하여 안지나간 배추와 구별
            graph[next_y][next_x] = -1
            dfs(next_y,next_x)

cases = int(input())
for t in range(cases):
    row, col, cabbage_num = map(int, input().split())

    graph = [[0]*row for _ in range(col)]
    for _ in range(cabbage_num):
        x,y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for y in range(col):
        for x in range(row):
            if graph[y][x] == 1:
                dfs(y,x)
                cnt += 1

    print(cnt)
