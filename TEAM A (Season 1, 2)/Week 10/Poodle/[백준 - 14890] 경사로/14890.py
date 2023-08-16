# 백준 14890번: 경사로 (2회차)

import sys

input = sys.stdin.readline

# N <= 10^2, L <= 10^2
N, L = map(int, input().rstrip().split())

maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 1. 해당 칸보다 높은 칸을 만난다면
# 2. 해당 칸보다 낮은 칸을 만난다면

answer = 0

# 가로 방향 길
for i in range(N):
    prev = maps[i][0]
    available = True
    visited = [False] * (N)

    for j in range(1, N):
        current = maps[i][j]

        # 높이가 같은 경우: 패스
        if prev == current:
            pass
        # 이전 칸 대비 1칸 높아지는 경우
        elif prev + 1 == current:
            cnt = 0

            # 이전 칸 포함 앞쪽으로 L칸의 높이가 같아야 함
            for k in range(L):
                if 0 <= j - k - 1 and maps[i][j - k - 1] == maps[i][j - 1] and not visited[j - k - 1]:
                    cnt += 1
                    visited[j - k - 1] = True
                else: break

            if cnt < L:
                available = False
                break
        # 이전 칸 대비 1칸 낮아지는 경우
        elif prev - 1 == current:
            cnt = 0

            # 현재 칸 포함 뒷쪽으로 L칸의 높이가 같아야 함
            for k in range(L):
                if j + k < N and maps[i][j + k] == maps[i][j] and not visited[j + k]:
                    cnt += 1
                    visited[j + k] = True
                else: break

            if cnt < L:
                available = False
                break
        else:
            available = False
            break

        prev = current

    if available: answer += 1

# 세로 방향 길
for j in range(N):
    prev = maps[0][j]
    available = True
    visited = [False] * (N)

    for i in range(1, N):
        current = maps[i][j]

        # 높이가 같은 경우: 패스
        if prev == current:
            pass
        # 이전 칸 대비 1칸 높아지는 경우
        elif prev + 1 == current:
            cnt = 0

            # 이전 칸 포함 앞쪽으로 L칸의 높이가 같아야 함
            for k in range(L):
                if 0 <= i - k - 1 and maps[i - k - 1][j] == maps[i - 1][j] and not visited[i - k - 1]:
                    cnt += 1
                    visited[i - k - 1] = True
                else: break

            # print(cnt)
            if cnt < L:
                available = False
                break
        # 이전 칸 대비 1칸 낮아지는 경우
        elif prev - 1 == current:
            cnt = 0

            # 현재 칸 포함 뒷쪽으로 L칸의 높이가 같아야 함
            for k in range(L):
                if i + k < N and maps[i + k][j] == maps[i][j] and not visited[i + k]:
                    cnt += 1
                    visited[i + k] = True
                else: break

            if cnt < L:
                available = False
                break
        else:
            available = False
            break

        prev = current

    if available: answer += 1

print(answer)
