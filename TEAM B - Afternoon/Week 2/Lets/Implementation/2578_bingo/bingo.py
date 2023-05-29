# 5x5 빙고판과 사회자가 부르는 숫자들이 주어짐
# 3줄을 채우면 빙고
# 몇번쨰 불렀을때 빙고가 되는지

# 1초 -> 25개의 판을 많이 돌아도 연산은 충분할 것 같으니, 그냥 구현해보자

import sys
sys.stdin = open("2578_bingo/bingo.txt", "r")


# 0. 각 줄의 빙고가 몇개인지 판단하는 함수들
def detect_row_bingo():
    cnt = 0
    for i in range(5):
        if sum(visited_matrix[i]) == 5:
            cnt += 1
    return cnt

def detect_col_bingo():
    cnt = 0
    cnt_arr = [0 for _ in range(5)]
    
    for i in range(5):
        for j in range(5):
            if visited_matrix[i][j] == 1:
                cnt_arr[j] += 1
    for i in range(5):
        if cnt_arr[i] == 5:
            cnt += 1
    return cnt

def detect_diagnal_bingo():
    cnt = 0
    up_to_down = 0
    down_to_up = 0

    for i in range(5):
        if visited_matrix[i][i] == 1:
            up_to_down += 1
        if visited_matrix[4-i][i] == 1:
            down_to_up += 1

    if up_to_down == 5:
        cnt += 1
    if down_to_up == 5:
        cnt += 1
    
    return cnt

# 1. 1줄~5줄 빙고판 만들기
matrix = []
for _ in range(5):
    matrix.append(list(map(int, sys.stdin.readline().split())))

# 1.5 해당 지점이 불렸는지 아닌지를 판단할 matrix
visited_matrix = [[0 for _ in range(5)] for _ in range(5)]

# 2. 6줄~10줄 사회자가 부르는 숫자들 정리
numbers = []

for _ in range(5):
    numbers += list(map(int, sys.stdin.readline().split()))

# 3. 5x5 에서 3줄 빙고가 되려면 최소 불러야하는 숫자의 갯수는 12개
# -> 12개까지는 그냥 채우고 그 이후로 빙고인지 아닌지 연산하자

# 근데 사회자가 부를때마다 2차원 배열을 도는건 귀찮다
# dict 에 숫자-matrix상의 좌표 를 key-value 로 넣어두고 그떄마다 꺼내 쓰자
coordinate_dict = {}

for i in range(5):
    for j in range(5):
        coordinate_dict[matrix[i][j]] = (i,j)


# 사회자가 11개 부르기
for i in range(0, 11):
    r, c = coordinate_dict[numbers[i]]
    visited_matrix[r][c] = 1

# 사회자가 12개 부르는 시점부터 detecting 시작
#### -> 미친넘 여기서 11부터 i 가 시작해야하는데, 그러지 않고 12부터 시작해서 계속 틀림 ###
for i in range(11, len(numbers)):
    flag = 0
    r, c = coordinate_dict[numbers[i]]
    visited_matrix[r][c] = 1

    flag = detect_row_bingo() + detect_col_bingo() + detect_diagnal_bingo()

    if flag >= 3:
        print(i+1) # 실제 숫자는 + 1
        break
