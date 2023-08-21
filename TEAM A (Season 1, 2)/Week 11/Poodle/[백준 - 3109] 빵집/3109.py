# 백준 3109번: 빵집

import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())

maps = [list(input().rstrip()) for _ in range(R)]
# for row in maps:
#     print(row)

next_moves = ((-1, 1), (0, 1), (1, 1))

visited = [[0 for _ in range(C)] for _ in range(R)]

def dfs(r, c):
    if c == C - 1:
        global answer
        answer += 1
        return True

    for dr, dc in next_moves:
        if 0 <= r + dr < R and 0 <= c + dc < C:
            if maps[r + dr][c + dc] == '.' and not visited[r + dr][c + dc]:
                visited[r + dr][c + dc] = 1
                if dfs(r + dr, c + dc):
                    return True
                
    return False

answer = 0
for r in range(R):
    visited[r][0] = 1
    dfs(r, 0)

print(answer)
