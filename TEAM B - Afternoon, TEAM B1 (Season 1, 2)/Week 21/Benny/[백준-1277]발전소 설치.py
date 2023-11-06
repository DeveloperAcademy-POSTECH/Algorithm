# https://www.acmicpc.net/problem/1277

import sys, heapq
from itertools import combinations
from collections import deque

input = sys.stdin.readline

def dist(a, b):
    dx, dy = pos[a][0] - pos[b][0], pos[a][1] - pos[b][1]
    return (dx**2 + dy**2) ** 0.5

INF = 987_654_321
n, w = map(int, input().split())
m = float(input())
pos = [(0, 0)]
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))

graph = [[] for _ in range(n+1)]
for _ in range(w):
    a, b = map(int, input().split())
    graph[a].append((0, b))
    graph[b].append((0, a))
    
    
for c in combinations(range(1, n+1), 2):
    a, b = c
    if dist(a, b) <= m:
        graph[a].append((dist(a, b), b))
        graph[b].append((dist(a, b), a))
    
# dijkstra
dists = [INF] * (n+1)
q = []
dists[1] = 0
heapq.heappush(q, (0, 1))

while q:
    d, node = heapq.heappop(q)
    for info in graph[node]:
        nd, next_node = info
        if dists[next_node] > d + nd:
            dists[next_node] = d + nd
            q.append((d+nd, next_node))
           
print(int(dists[n] * 1000))
    