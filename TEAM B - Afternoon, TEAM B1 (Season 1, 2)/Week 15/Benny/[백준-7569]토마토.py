from collections import deque

m, n, h = map(int, input().split())
tomatoes = []
for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    tomatoes.append(temp)

# 익은 토마토의 좌표
coords = deque([[i, j, k] for i in range(h) for j in range(n) for k in range(m) if tomatoes[i][j][k] == 1])

# 위, 아래, 뒤, 앞, 왼쪽, 오른쪽
dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

while coords:
    cur_i, cur_j, cur_k = coords.popleft()
    for idx in range(6):
        new_i = cur_i + dz[idx]
        new_j = cur_j + dy[idx]
        new_k = cur_k + dx[idx]
        
        if 0 <= new_i < h and 0 <= new_j < n and 0 <= new_k < m:
            if tomatoes[new_i][new_j][new_k] == 0:
                tomatoes[new_i][new_j][new_k] = tomatoes[cur_i][cur_j][cur_k] + 1
                coords.append([new_i, new_j, new_k]) 
#            elif tomatoes[new_i][new_j][new_k] > tomatoes[cur_i][cur_j][cur_k] + 1:
#                tomaotes[new_i][new_j][new_k] = tomatoes[cur_i][cur_j][cur_k] + 1
#                coords.append([new_i, new_j, new_k]) 

# 끝까지 0(익지 않은 토마토)이 남아있을 경우를 확인하기 위한 zeros / max를 사용하여 최댓값을 확인해 전체 토마토가 익는데 걸린 시간을 확인하기 위한 flatten
# zeros = [tomatoes[i][j][k] for i in range(h) for j in range(n) for k in range(m) if tomatoes[i][j][k] == 0]
flatten = [tomatoes[i][j][k] for i in range(h) for j in range(n) for k in range(m)]

# 0 이 남아있으면 모든 토마토를 익힐 수 없으므로 -1 출력 / 그렇지 않다면 모든 토마토가 익은 것이므로 '최댓값 -1'(처음부터 익어있던 토마토에 영향 받은 토마토들은 2부터 시작했으므로) 출력
if 0 in flatten:
    print(-1)
else:
    print(max(flatten) - 1)
    