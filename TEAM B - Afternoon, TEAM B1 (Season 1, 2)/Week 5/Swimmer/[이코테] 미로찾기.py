from collections import deque

#  N, M 을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
maze = []
for i in range(n):
    maze.append(list(map(int,input())))

# 방문 기록용 2차원 리스트
check = [[0]*m for _ in range(n)]

# 이동칸 기록용 2차원 리스트
count = [[0]*m for _ in range(n)]

# 상하좌우 이동용 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스 코드 구현
def bfs():

    # bfs 탐색용 큐 생성
    queue = deque()

    # 시작 위치를 큐에 삽입
    queue.append((0,0))
    # 시작 위치 방문 기록
    check[0][0] = 1
    # 시작 위치 이동칸 수 기록
    count[0][0] = 1

    # queue 의 요소가 전부 제거될 때까지 반복
    while queue:
        # 큐의 최하단 요소를 현재 위치로 저장하고 큐에서 제거
        x, y = queue.popleft()

        # 현재 위치를 기준으로 상하좌우 탐색
        for i in range(4):

            # 인접한 노드의 위치
            nx = x + dx[i]
            ny = y + dy[i]

            # 인접한 노드가 미로 내부에 존재하는지 확인
            if (nx >=0 and nx < n and ny >= 0 and ny < m):

                # 인접한 노드를 방문할 수 있는지 확인
                if (check[nx][ny] == 0 and maze[nx][ny] == 1):

                    # 방문할 수 있다면 큐에 삽입
                    queue.append((nx,ny))
                    # 인접 노드 방문 기록
                    check[nx][ny] = 1
                    # 인접 노드 이동칸 수 기록
                    count[nx][ny] = count[x][y] + 1

    return count[n-1][m-1]

print(bfs())