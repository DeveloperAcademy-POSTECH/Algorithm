# 백준 토마토 2
# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

sys.stdin = open("7569_tomato2/tomato2.txt", "r")
# 결국 m x n 상자가 H 층 쌓아올려지는 3차원 배열

def checkCube():
    for h in range(H):
        for r in range(R):
            for c in range(C):
                if cube[h][r][c] == 0:
                    print(-1)
                    return False
    return True

# 일단 m, n, h 입력받기
C, R, H = list(map(int, sys.stdin.readline().split()))

#  3차원 배열 생성
cube = []

# 3차원 배열에 값 넣기 -> 이게 제일 어렵네
for h in range(H):
    matrix = []
    for r in range(R):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    cube.append(matrix)

# print(cube)

# 토마토 익는걸 계산
# 어캐 하느냐? 


# 1. 우선 3차원을 다 돌면서 익은 토마토(숫자 1) 을 찾는다
# 2. 찾으면 deque 든 stack 이든 queue (container) 에 넣는다
dq = deque()

for h in range(H):
    for r in range(R):
            for c in range(C):
                # print(h, r, c)
                if cube[h][r][c] == 1:
                    dq.append((h,r,c))


# 3. 다 돌면서 넣었으면 이제 하나씩 pop 하면서 해당 위치에 위,아래,앞,뒤,좌,우 를 체크해서 
days = 0

dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


while dq:
    # print(dq)
    size = len(dq)
    for _ in range(size):
        h, r, c = dq.popleft()

        for i in range(6):
            nh = h + dh[i]
            nr = r + dr[i]
            nc = c + dc[i]

            if not((0<=nh<H) and (0<=nr<R) and (0<=nc<C)): # 범위를 벗어나면 바로 해당 루프 탈출
                continue

            if cube[nh][nr][nc] == 0: 
                cube[nh][nr][nc] = 1 # 토마토가 덜익은(0)이면 1로 바꿔주고
                dq.append((nh, nr, nc)) # 익은 토마토로 다시 container 에 넣는다.
            
    # 이걸 하루라 치고 하루를 기록하는 int 형 변수 += 1 을 해준다.
    days += 1



# 해당 작업을 container 가 다 빌때까지 반복한다.


# 다 비었으면, 3차원 상자 전체를 탐색한다.

# print(cube)
            
if checkCube():
    print(days-1)
# 다 익었으면 0을 출력, 아니면 -1 을 출력



# 어려움을 겪은점
# 1. 일단 파이썬 너무 어색했음. input 받는거나 .txt 에서 읽게 하는것에서부터 변수선언, 함수 만들기 등등 기본이 부족함을 느낌
# 2. index 에러 계속 나서 힘들었음. 머리속으로 생각한 방법은 맞았는데 계속 구현에서 시간이 끌림
# 3. 다차원 list 가 저장되는걸 머리로만 생각하니까 어려웠음. 그려봤으면 더 편했으려나
