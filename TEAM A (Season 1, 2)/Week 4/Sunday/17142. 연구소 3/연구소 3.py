import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
virus=[]
wall = 0 #벽갯수
#바이러스놈의 위치와 벽개수부터 찾자       
for i in range(N):
    for j in range(N):
        if(graph[i][j] == 2):
            virus.append((i,j))
        elif graph[i][j] == 1 :
            wall += 1
def BFS(virusdata):
    q = deque()
    visited = [[-1]* N for _ in range(N)] #일단 -1로 세팅
    temp = 0
    cnt = 0
    for x,y in virusdata:
        q.append((x,y))
        visited[x][y] = 0 # 활성화된 애들은 일단 방문했으니
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0<=nx<N and 0<=ny < N and visited[nx][ny] == -1 and graph[nx][ny] != 1): #방문안한놈들 + 벽이 아닌곳만 가자
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
                if(graph[nx][ny]==0):
                    temp = max(temp, visited[nx][ny]) 
    for row in visited:
        for element in row:
            if element == -1:
                cnt += 1
    if cnt != wall:
        return sys.maxsize
    return temp
                
                
ans = sys.maxsize                
for virusdata in list(combinations(virus, M)):
    ans = min(BFS(virusdata), ans)
if(ans == sys.maxsize):
    print(-1)
else:
    print(ans)
