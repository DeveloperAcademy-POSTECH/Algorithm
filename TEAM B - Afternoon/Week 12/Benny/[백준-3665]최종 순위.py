#https://www.acmicpc.net/problem/3665
#백준-3665-최종 순위
#위상정렬

import sys
from collections import deque

input = sys.stdin.readline

def get_graph(ranking):
    graph = [ [] for _ in range(len(ranking) + 1)]
    for i in range(len(ranking)):
        graph[ranking[i]] = ranking[:i]
    
    return graph

def change_ranking(graph, a, b):
    if a in graph[b]:
        graph[b].remove(a)
        graph[a].append(b)
    if b in graph[a]:
        graph[a].remove(b)
        graph[b].append(a)
        
    return graph

t = int(input())
for _ in range(t):
    n = int(input())
    ranking = list(map(int, input().split()))
    graph = get_graph(ranking)
    
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
        else:
            graph[a].remove(b)
            graph[b].append(a)
            
    indegrees = [n-1-len(graph[i]) for i in range(len(graph))]
    
    q = deque([])
    for i in range(1, len(indegrees)):
        if indegrees[i] == 0:
            q.append(i)
            
    result = []
    while q:
        now_team = q.popleft()
        result.append(now_team)
        for next_team in graph[now_team]:
            indegrees[next_team] -= 1
            if indegrees[next_team] == 0:
                q.append(next_team)
                
    if len(result) == n:
        print(' '.join(map(str, reversed(result))))
    else:
        print("IMPOSSIBLE")
                
            
        