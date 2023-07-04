# https://www.acmicpc.net/problem/1916
# 백준-1916-최소비용 구하기

import sys, heapq

input = sys.stdin.readline
INF = int(1e8)

N = int(input())
M = int(input())
graph = [{} for i in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    if graph[u].get(v) == None:
        graph[u][v] = w
    elif w < graph[u][v]:
        graph[u][v] = w
    
start, end = map(int, input().split())

costs = [INF] * (N+1)
q = []
heapq.heappush(q, (0, start))
while q:
    c, now = heapq.heappop(q)
    for target in graph[now].keys():
        if c + graph[now][target] < costs[target]:
            costs[target] = c + graph[now][target]
            heapq.heappush(q, (costs[target], target))
            
print(costs[end])
