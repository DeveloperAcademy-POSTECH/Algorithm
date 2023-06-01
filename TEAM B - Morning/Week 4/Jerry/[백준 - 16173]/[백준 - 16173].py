import sys

def dfs(x,y) :
    if x<=-1 or x>=N or y<=-1 or y>=N or visit[x][y]==1:
        return
    if graph[x][y] == -1 :
        visit[x][y] = 2
        return
    visit[x][y]=1
    dfs(x+graph[x][y],y)
    dfs(x,y+graph[x][y])


N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

visit=[[0]*N for _ in range(N)]
dfs(0,0)

if visit[-1][-1] == 2 :
    print('HaruHaru')
else :
    print('Hing')