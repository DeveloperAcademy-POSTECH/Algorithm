#https://www.acmicpc.net/problem/1753
# 백준-1753-최단경로

import sys, heapq

input = sys.stdin.readline

INF = int(1e10)

V, E = map(int, input().split())
K = int(input())
graph = [[] for i in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    
distances = [INF] * (V+1)
distances[K] = 0
q = []
heapq.heappush(q, (0, K))
while q:
    d, now = heapq.heappop(q)
    for info in graph[now]:
        if d + info[1] < distances[info[0]]:
            distances[info[0]] = d + info[1]
            heapq.heappush(q, (distances[info[0]], info[0]))
            
for i in range(1, len(distances)):
    if distances[i] == INF:
        print('INF')
    else:
        print(distances[i])
