v = int(input())
m = int(input())
cur_v = 1

# 그래프 초기화
graph = [[0]*(v+1) for i in range(v+1)]

# 입력받아서 그래프에 값 넣기
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

# dfs 혹은 bfs를 통해 visited한 목록 구하기
visited = [False] * (v+1)
visited[1] = True
def dfs(cur_v):
    visited[cur_v] = True
    for i in range(1, v+1):
        if visited[i] == False and graph[cur_v][i] == 1:
            dfs(i)
    return visited.count(1) - 1

print(dfs(1))