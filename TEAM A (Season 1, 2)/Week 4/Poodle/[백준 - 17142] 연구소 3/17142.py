# 백준 17142번: 연구소 3

from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

# N <= 50, M <= 10
N, M = map(int, input().rstrip().split())

maps = [list(map(int, input().rstrip().split())) for _ in range(N)]
total_viruses = []

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

for r in range(N):
    for c in range(N):
        if maps[r][c] == 2:
            total_viruses.append((r, c))

def bfs(viruses):
    # print(viruses)

    q = deque()
    visited = [[-1 for _ in range(N)] for _ in range(N)]

    for r, c in viruses:
        q.append((r, c, 0))
        visited[r][c] = 0

    while q:
        # print(q)
        r, c, depth = q.popleft()

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                if maps[r + dr][c + dc] != 1 and visited[r + dr][c + dc] == -1:
                    q.append((r + dr, c + dc, depth + 1))
                    visited[r + dr][c + dc] = depth + 1
    
    # for row in visited:
    #     print(row)

    max_visited = 0
    for r in range(N):
        for c in range(N):    
            if maps[r][c] != 1 and visited[r][c] == -1:
                return -1
            
            if maps[r][c] != 1 and maps[r][c] != 2:
                max_visited = max(max_visited, visited[r][c])
    
    return max_visited

answer = int(1e9)

for viruses in combinations(total_viruses, M):
    current = bfs(viruses)

    # print(current)
    # print()

    if current != -1:
        answer = min(answer, current)

if answer < int(1e9):
    print(answer)
else:
    print(-1)
