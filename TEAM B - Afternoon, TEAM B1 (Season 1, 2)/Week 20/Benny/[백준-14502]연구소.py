# https://www.acmicpc.net/problem/14502

import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

def bfs(map2):
    q = deque([])
    for r in range(n):
        for c in range(m):
            if map2[r][c] == 2:
                q.append((r, c))
    
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and map2[nr][nc] == 0:
                map2[nr][nc] = 2
                q.append((nr, nc))
    
def find_safe_area(map2):
    count = 0
    for r in range(len(map2)):
        for c in range(len(map2[0])):
            if map2[r][c] == 0:
                count += 1
                
    return count

n, m = map(int, input().split())
map1 = []
for _ in range(n):
    map1.append(list(map(int, input().split())))
    
max_safe_area = 0
wall_combis = combinations([i for i in range(n * m)], 3)
for wc in wall_combis:
    w1, w2, w3 = map(lambda x: (x // m, x % m), wc)
    if map1[w1[0]][w1[1]] == 0 and map1[w2[0]][w2[1]] == 0 and map1[w3[0]][w3[1]] == 0:
        map2 = copy.deepcopy(map1)
        map2[w1[0]][w1[1]] = 1
        map2[w2[0]][w2[1]] = 1
        map2[w3[0]][w3[1]] = 1
        bfs(map2)
        max_safe_area = max(max_safe_area, find_safe_area(map2))
        
print(max_safe_area)