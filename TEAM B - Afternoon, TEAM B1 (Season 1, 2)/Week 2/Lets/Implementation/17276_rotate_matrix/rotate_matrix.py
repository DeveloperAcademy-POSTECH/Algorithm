# nxn 2차원 배열
# 45도 회전
# 4가지 연산이 동시적용
# 대각선, 수직선, 수평선을 45도로 끌어내리는게 45도 회전
# 그렇다면 반대가 -45도 회전이겠지?

# 시계 반시계방향 돌리기
# 시간제한 3초

# 첫줄에 테스트케이스 T
# 배열의 크기 최대 500 x 500 -> n^3 -> 125000000 -> 1.25억이니까 괜찮은듯?
# 돌려야하는 각도 d -> 양수 음수 구분
# n 줄에 걸쳐 matrix 가 주어짐

import sys
sys.stdin = open("17276_rotate_matrix/rotate_matrix.txt", "r")

# 테스트케이스 수
tc = int(sys.stdin.readline())


def rotate():
    # 1. 주 대각선을 가운대열로
    for i in range(n):
        rotated_matrix[i][n//2] = matrix[i][i]

    # 2. 가운대열을 부 대각선으로
    for i in range(n):
        rotated_matrix[i][n-i-1] = matrix[i][n//2]

    # 3. 부 대각선을 가운데 행으로
    for i in range(n):
        rotated_matrix[n//2][n-i-1] = matrix[i][n-i-1]

    # 4. 가운데 행을 주 대각선으로
    for i in range(n):
        rotated_matrix[i][i] = matrix[n//2][i] 

    # 5. 기존의 matrix 에 변형된 matrix 옮겨넣기
    for i in range(n):
        matrix[i] = rotated_matrix[i][:]
    # for row in rotated_matrix:
    #     print(row)
    # print()
    # pass

def rotate_reverse():
    # 1.
    for i in range(n):
        rotated_matrix[n//2][i] = matrix[i][i]

    # 2.
    for i in range(n):
        rotated_matrix[n-i-1][i] = matrix[n//2][i] 
    # 3. 
    for i in range(n):
        rotated_matrix[i][n//2] = matrix[i][n-i-1]

    # 4.
    for i in range(n):
        rotated_matrix[i][i] = matrix[i][n//2]
    # 5.
    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated_matrix[i][j]
    # for i in range(n):
    #     for j in range(n):
    #         if rotated_matrix[i][j] == "0":
    #             rotated_matrix[i][j] = matrix[i][j]
    # for row in rotated_matrix:
    #     print(row)
    # print()


for t in range(1, tc+1):
    # n 과 d
    n, d = list(map(int, sys.stdin.readline().split()))

    # 회전 전 matrix
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    # 회전 후 matrix
    rotated_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix[i][j] = matrix[i][j]

    # 회전 방향과 횟수 설정
    reverse = True if d < 0 else False

    times = (abs(d) // 45) % 8  # 회전 횟수 계산 -> 아 미친넘 360 / 45 가 4냐 8이지

    if reverse:
        for _ in range(times):
            rotate_reverse()
    else:
        for _ in range(times):
            rotate()


    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()
                
