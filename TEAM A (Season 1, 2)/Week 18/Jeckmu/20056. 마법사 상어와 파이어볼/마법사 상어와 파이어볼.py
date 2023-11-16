N, M, K = map(int, input().split())

# 방향 (r이동량, c이동량)
directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

fireballs = []
for i in range(M):
    fireballs.append(list(map(int, input().split())))
    
# 이동 후 파이어볼의 위치를 나타내기 위한 그래프(격자)
graph = [[[] for _ in range(N)] for _ in range(N)]
    
def move(g):
    for i, fireball in enumerate(fireballs):
        r, c, m, s, d = fireball
        dr, dc = directions[d]
        # 이동량 계산 및 MOD 연산을 통한 1번-N번 행/열 연결.
        r = (r + dr * s) % N
        c = (c + dc * s) % N
        
        # 이동 후 좌표 갱신
        fireballs[i][0] = r
        fireballs[i][1] = c
        
        # 이동 후 위치 저장
        g[r][c].append(i)

def collision(g):
    newBalls = []
    delIndex = []
    for r in range(N):
        for c in range(N):
            balls = g[r][c]
            # 칸에 있는 파이어볼이 2개 이상이면
            if len(balls) > 1:      
                # 합쳐진 파이어볼은 지우기 위해 저장
                delIndex.extend(balls)
                          
                # 질량 계산
                mass = 0
                for i in balls:
                    mass += fireballs[i][2]
                mass = mass//5
                if mass == 0:
                    continue
                
                # 속력 계산
                speed = 0
                for i in balls:
                    speed += fireballs[i][3]
                speed = speed//len(balls)
                
                # 방향 계산
                direction = 0
                for i in balls:
                    direction += fireballs[i][4] % 2
                
                # 파이어볼 나누기
                # 방향을 2로 나눈 나머지를 모두 더한 값이 0이거나 파이어볼의 개수와 같다면,
                # 방향이 모두 홀수이거나 짝수인 것.
                if direction == 0 or direction == len(balls):
                    for d in range(0, 8, 2):
                        newBalls.append([r, c, mass, speed, d])
                else:
                    for d in range(1, 9, 2):
                        newBalls.append([r, c, mass, speed, d])
                
                
    
    # 지우기 위해 저장했던 합쳐진 파이어볼 지우기
    delIndex = sorted(delIndex, reverse=True)
    for i in delIndex:
        del fireballs[i]
    # 새로운 파이어볼 추가
    fireballs.extend(newBalls)

# K회 실행
for _ in range(K):
    move(graph)
    collision(graph)
    # 그래프 초기화
    graph = [[[] for _ in range(N)] for _ in range(N)]

result = 0
for i in range(len(fireballs)):
    result += fireballs[i][2]

print(result)