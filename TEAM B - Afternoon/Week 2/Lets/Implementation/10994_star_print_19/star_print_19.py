# 예제를 보고 규칙을 유츄한 뒤에 별을 찍어보자
# 1x1, 5x5, 9x9, 13 x 13 ...
# 0,    1,   2,   3 ....
# 4n+1 ?
# -> 그리고 안으로 한칸씩 들어가면서 테두리 전체를 칠하고, 안칠하고를 반복

# N 최대가 100이니까 n^3 찍어도 1초안에 가능

import sys
sys.stdin = open("10994_star_print_19/star_print_19.txt","r")
N =  int(sys.stdin.readline())

# 배열을 돌면서 해당 테두리를 색칠하는 함수
def color_matrix(offset):
    # 위에
    for i in range(offset, n-offset):
        matrix[offset][i] = "*"

    # 아래
    for i in range(offset, n-offset):
        matrix[n-offset-1][i] = "*"

    # 왼쪽
    for i in range(offset, n-offset):
        matrix[i][offset] = "*"

    # 오른쪽
    for i in range(offset, n-offset):
        matrix[i][n-offset-1] = "*"



# 내가 유추한 배열의 한변의 길이
n = 4 * (N-1) + 1

# 배열 만들기
matrix = [[" " for _ in range(n)] for _ in range(n)]

# 돌아가면서 배열 색칠
for offset in range(n):
    if offset % 2 == 0:
        color_matrix(offset)
    else:
        pass

for row in matrix:
    print("".join(row))


