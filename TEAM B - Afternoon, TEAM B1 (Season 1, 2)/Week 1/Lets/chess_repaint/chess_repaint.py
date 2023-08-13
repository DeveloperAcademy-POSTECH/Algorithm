# 브루트 포스 문제니까 일단 처음부터 다 돌면서 체크해보자
# 1. 일단은 8 x 8 정사각형으로 자르고 -> 검사 범위를 이걸로 제한
# 2. 자른 정사각형 안에서 시작이 w 인지 b 인지 확인하고 
# -> 아.. 가장 처음의 것을 기준으로 두는게 아니라 하나의 8 x 8 에서 두가지 다 검사를 해야하는구나...
# 3. 교차되서 잘 나오는지 아닌지를 확인해보고, 이상한 색깔로 되어있으면 cnt 를 추가하자
# 4. 이 과정을 모든 8 x 8 에 적용해서 글로벌 최소를 구하자

# 근데 여기서 따로 w b 순서 체스판, 혹은 b w 체스판을 만들고 하는게 나을까 아니면 짝수 홀수에 따라서 판별하는게 빠를까?
# 내 생각에는 짝수 홀수로 하면 짝수 홀수인지 한번, 그에 맞는 색인지 2번 검사를 해야할것 같은데...
# 그러면 둘 다 해보지 뭐 


import sys

sys.stdin = open("chess_repaint/chess_repaint.txt", "r")

M, N = list(map(int, sys.stdin.readline().split()))

matrix = []

min_val = M * N

for _ in range(M):
    matrix.append(list(sys.stdin.readline().rstrip()))

## 미리 wb 체스판을 만들어놓고 사용하는 함수를 위한 code
bw_line = ["W" if i % 2 else "B"  for i in range(8)]
wb_line = ["B" if i % 2 else "W"  for i in range(8)]

wb_matrix = [] # wb 체스판
for i in range(8):
    if i % 2 == 0:
        wb_matrix.append(wb_line)
    else:
        wb_matrix.append(bw_line)



bw_matrix = [] # bw 체스판
for i in range(8):
    if i % 2 == 0:
        bw_matrix.append(bw_line)
    else:
        bw_matrix.append(wb_line)




# 1. 범위마다 돌면서 체크하는 함수 
def divide_chess():
    global min_val

    # 가로,세로 범위의 시작은 m-8, n-8 부터, # 시작점을 세팅해주는 for 문들
    if M == 8 and N == 8:
        min_val = min(min_val, different_check(0, 0))
        return
    
    for i in range(0, M-7):
        for j in range(0, N-7):

            # print(i, j)
            min_val = min(min_val,different_check(i, j))


## 미리 wb 교차되는걸 만들어놓고 사용하는 함수
# 3. 교차되는게 잘 나오는지 확인하는 함수
def check_chess(i, j):
    wb_cnt = 0 # wb 검사를 했을때 틀린갯수를 체크하는 변수
    for dr in range(8): # dr 은 row 의 변화량
        # print(matrix[i_start+dr])
        for dc in range(8): # dc 는 col 의 변화량
            if matrix[i+dr][j+dc] != wb_matrix[dr][dc]:
                wb_cnt += 1

    bw_cnt = 0 # wb 검사를 했을때 틀린갯수를 체크하는 변수
    for dr in range(8): # dr 은 row 의 변화량
        for dc in range(8): # dc 는 col 의 변화량
            if matrix[i+dr][j+dc] != bw_matrix[dr][dc]:
                bw_cnt += 1


    # 가장 적게 바꾸면 되는것을 return
    return min(wb_cnt, bw_cnt)





def different_check(i, j):
    wb_cnt = 0 # wb 검사를 했을때 틀린갯수를 체크하는 변수
    for dr in range(8): # dr 은 row 의 변화량
        # print(matrix[i_start+dr])
        for dc in range(8): # dc 는 col 의 변화량
                if dr % 2 == 0:
                    if dc % 2 == 0:
                        if matrix[i+dr][j+dc] != "B":
                            wb_cnt += 1
                    else:
                        if matrix[i+dr][j+dc] != "W":
                            wb_cnt += 1
                else:
                    if dc % 2 == 0:
                        if matrix[i+dr][j+dc] != "W":
                            wb_cnt += 1
                    else:
                        if matrix[i+dr][j+dc] != "B":
                            wb_cnt += 1

    bw_cnt = 0 # wb 검사를 했을때 틀린갯수를 체크하는 변수
    for dr in range(8): # dr 은 row 의 변화량
        for dc in range(8): # dc 는 col 의 변화량
            if dr % 2 == 0:
                if dc % 2 == 0:
                    if matrix[i+dr][j+dc] != "W":
                        bw_cnt += 1
                else:
                    if matrix[i+dr][j+dc] != "B":
                        bw_cnt += 1
            else:
                if dc % 2 == 0:
                    if matrix[i+dr][j+dc] != "B":
                        bw_cnt += 1
                else:
                    if matrix[i+dr][j+dc] != "W":
                        bw_cnt += 1


    # 가장 적게 바꾸면 되는것을 return
    return min(wb_cnt, bw_cnt)       
    

divide_chess()
print(min_val)



# 방법 1. 미리 정답 체스판을 만들어놓고 비교(check_chess 함수) -> 68ms
# 방법 2. 매번 bwbw.... wbwb... 비교(different_check 함수) -> 84ms
# 차이가...있다...!


# 문제 풀면서 어려웠던점

# 1. 
# 자꾸 index out of range 에러가 남
# 뭐지? 하고 한시간 찾음
# 알고보니 문제에서 통상적인 M, N 의 값을 거꾸로 줌... :(

# 2. 
# index 계산이 빡세서 그냥 값 계속 바꿔 넣어가면서 했음
# 그런데 그냥 처음부터 잘 계산 할 줄 알게 되야겠다. 매번 런타임 에러를 볼 순 없음