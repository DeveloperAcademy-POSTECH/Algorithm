from collections import deque

node, edge, startV = map(int, input().split())
graph = [[0]*(node+1) for _ in range(node+1)]
for i in range(edge):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1
nodeStatus = [0]*(node+1)

# bfs
def bfs(graph, startV):
    queue = deque([startV])
    nodeStatus[startV] = 1
    while queue:
        cur_v = queue.popleft()
        print(cur_v, end=" ")
        for i in range(1, node+1):
            if nodeStatus[i] == 0 and graph[cur_v][i] == 1:
                queue.append(i)
                nodeStatus[i] = 1

nodeStatusDFS = [False]*(node+1) 
visitedDFS = []
cur_v = startV
# dfs
def dfs(cur_v):
    print(cur_v, end =" ")
    nodeStatusDFS[cur_v] = True
    for i in range(1,node+1):
        if not nodeStatusDFS[i] and graph[cur_v][i] == 1:
            dfs(i)
    
dfs(cur_v)
print()
bfs(graph,startV)

