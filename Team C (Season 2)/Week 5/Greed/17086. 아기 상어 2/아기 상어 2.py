from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    dx = [0, 0, -1, 1, -1, 1, 1, -1]
    dy = [1, -1, 0, 0, 1, 1, -1, -1]
    queue = deque()
    # 상어가 있는 곳만 계산
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i,j))
    longest = 0
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(8):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            # graph의 index를 벗어나지 않으면서, 방문하지 않은 곳이면서, 아기상어가 없는 곳
            if next_x in range(n) and next_y in range(m):
                if not graph[next_x][next_y]:
                    queue.append((next_x,next_y))
                    graph[next_x][next_y] = graph[cur_x][cur_y] + 1
                    longest = graph[next_x][next_y]
    return longest

print(bfs()-1)