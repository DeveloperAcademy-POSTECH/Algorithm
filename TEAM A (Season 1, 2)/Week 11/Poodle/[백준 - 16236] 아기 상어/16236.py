# 백준 16236번: 아기 상어 (2회차)

from collections import deque
import sys

input = sys.stdin.readline

# N <= 20
N = int(input())

maps = [list(map(int, input().rstrip().split())) for _ in range(N)]
# for row in maps:
#     print(row)
# print()

shark_size = 2
shark_eat = 0
shark_r, shark_c = -1, -1
for r in range(N):
    for c in range(N):
        if maps[r][c] == 9:
            shark_r, shark_c = r, c
            maps[r][c] = 0

moves = ((-1, 0), (0, -1), (1, 0), (0, 1))
answer = 0

def bfs(r, c):
    global shark_size, shark_eat, shark_r, shark_c
    global answer

    q = deque()
    visited = [[-1 for _ in range(N)] for _ in range(N)]

    q.append((r, c, 0))
    visited[r][c] = 0

    found = False
    fish_r, fish_c = N, N
    shark_moved = -1

    while q:
        r, c, moved = q.popleft()

        if found and shark_moved < moved:
            break
        elif 0 < maps[r][c] < shark_size:
            found = True

            if fish_r > r or (fish_r == r and fish_c > c):
                fish_r, fish_c = r, c
                shark_moved = moved

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                if maps[r + dr][c + dc] <= shark_size and visited[r + dr][c + dc] == -1:
                    q.append((r + dr, c + dc, moved + 1))
                    visited[r + dr][c + dc] = moved + 1

    if found:
        shark_r, shark_c = fish_r, fish_c # 해당 물고기 장소로 이동
        maps[fish_r][fish_c] = 0 # 물고기 사라짐
        shark_eat += 1 # 상어 먹은 개수 증가

        # 상어가 자신의 사이즈만큼 물고기를 먹었다면
        if shark_size <= shark_eat:
            shark_size += 1
            shark_eat = 0

        answer += shark_moved
        return True
    else:
        return False

while True:
    found = bfs(shark_r, shark_c)

    # for row in maps:
    #     print(row)
    # print(shark_size, shark_eat, shark_r, shark_c)
    # print(answer)
    # print()

    if not found: break

print(answer)
