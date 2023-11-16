from collections import deque
N, M = map(int, input().split())

# 미로 입력
miro = []
for _ in range(N):
    miro.append(list(input()))

# 시작 좌표 ("0") 탐색
start = ()
for r in range(N):
    for c in range(M):
        if miro[r][c] == "0":
            start = (r, c)

# visited[r][c][flag]에 각 방문에서의 이동 횟수를 저장.
# flag 값은 A, B, C, D, E, F의 열쇠를 가지고 있는 지에 따라 BitMasking으로 저장. 
# (111111 => A ~ F의 열쇠를 가짐 / 101000 => A, C의 열쇠를 가지고 있음.)
INF = 10e9
visited = [[[INF for _ in range((1 << 6))] for _ in range(M)] for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# BFS
deq = deque([(start[0], start[1], 0, 0)])

while deq:
    r, c, cnt, flag = deq.popleft()
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 미로 벗어남 여부 체크 및 visited 체크
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][flag] == INF:
            if miro[nr][nc] == "#":    # 벽
                continue
            elif miro[nr][nc] == ".":   # 빈칸
                deq.append((nr, nc, cnt+1, flag))
                visited[nr][nc][flag] = cnt+1
            elif 97 <= ord(miro[nr][nc]) <= 102:    # a ~ f 열쇠 칸
                # 아스키코드, BitMasking을 통해 열쇠 보유 여부를 추가.
                o = ord(miro[nr][nc]) - 97
                newFlag = flag | (1 << o)
                deq.append((nr, nc, cnt+1, newFlag))
                visited[nr][nc][newFlag] = cnt+1
            elif 65 <= ord(miro[nr][nc]) <= 70:     # A ~ F 문 칸
                o = ord(miro[nr][nc]) - 65
                if flag & (1 << o):     # 열쇠가 있는 지 확인 (BitMasking)
                    deq.append((nr, nc, cnt+1, flag))
                    visited[nr][nc][flag] = cnt+1
            elif miro[nr][nc] == "1":   # 달이 차오르는 위치 칸
                visited[nr][nc][flag] = min(visited[nr][nc][flag], cnt+1)
            elif miro[nr][nc] == "0":
                deq.append((nr, nc, cnt+1, flag))
                visited[nr][nc][flag] = cnt+1

result = INF
for r in range(N):
    for c in range(M):
        if miro[r][c] == "1":
            result = min(min(visited[r][c]), result)

if result == INF:
    print(-1)
else:
    print(result)