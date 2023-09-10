from collections import deque

N = int(input())
M = []
for _ in range(N):
    M.append(list(map(int, input().split())))

# 상어를 찾고, 상어 칸을 2로 설정.
shark = ()
for i in range(N):
    for j in range(N):
        if M[i][j] == 9:
            shark = (i, j)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c):
    visited = [[0]*N for _ in range(N)]
    # 1로 설정해야 시작한 곳을 queue에 append하지 않음.
    visited[r][c] = 1
    deq = deque([(r, c)])
    prey = []

    while deq:
        i, j = deq.popleft()

        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]

            # 범위 내인지, 이미 visit했는지 확인
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                # 먹을 수 있으면
                if M[r][c] > M[nr][nc] and M[nr][nc] != 0:
                    # 이전 visited보다 +1 함으로써, 몇 초가 걸리는 지 저장
                    visited[nr][nc] = visited[i][j]+1
                    prey.append((visited[nr][nc]-1, nr, nc))
                # 숫자가 같을 때 (지나갈 수만 있음)
                elif M[r][c] == M[nr][nc]:
                    visited[nr][nc] = visited[i][j]+1
                    deq.append((nr, nc))
                # 빈 칸일 때
                elif M[nr][nc] == 0:
                    visited[nr][nc] = visited[i][j]+1
                    deq.append((nr, nc))

    # 먹을 수 있는 리스트를 반환. 가장 가까운 것 -> 가장 위 -> 가장 왼쪽 순으로 나열.
    return list(sorted(prey, key=lambda x: (x[0], x[1], x[2])))


second = 0
size = 2
eat = 0

while True:
    r, c = shark
    M[r][c] = size

    prey = list(bfs(r, c))
    # 먹이가 없으면 break
    if not prey:
        break

    # 먹이가 있으면, 최우선순위의 먹이를 먹음.
    sec, nr, nc = prey[0]

    second += sec
    eat += 1

    if eat == size:
        size += 1
        eat = 0

    M[r][c] = 0
    shark = (nr, nc)

print(second)