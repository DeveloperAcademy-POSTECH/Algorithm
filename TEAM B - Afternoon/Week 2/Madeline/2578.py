# 2578

import sys

# input 함수가 이걸로 바뀐다, 시간을 줄여준다고 한다,,
input = sys.stdin.readline


# 해당 숫자를 찾아서 그 숫자의 index를 반황하는 함수
def find_num(a):
    for i in range(0, 5):
        for j in range(0, 5):
            if a == myBingo[i][j]:
                return i * 5 + j


def count_bingo(i):
    bingo1 = bingo2 = bingo3 = bingo4 = 0
    bingo1_tmp = [0, 0, 0, 0, 0]
    bingo2_tmp = [0, 0, 0, 0, 0]

    # 가로 빙고 : index / 5가 같은 수
    for j in range(0, i+1):
        k = int(index[j] / 5)
        bingo1_tmp[k] += 1

    # 세로 빙고 :  index % 5가 같은 수
    for j in range(0, i+1):
        k = int(index[j] % 5)
        bingo2_tmp[k] += 1

    # 가로, 세로 빙고 개수 세기
    for j in range(0, 5):
        if bingo1_tmp[j] >= 5:
            bingo1 += int(bingo1_tmp[j] / 5)

        if bingo2_tmp[j] >= 5:
            bingo2 += int(bingo2_tmp[j] / 5)

    # 대각선 빙고 - 1: index%6==0
    for j in range(0, i+1):
        if j % 6 == 0:
            bingo3 += 1
        # 대각선 빙고 - 2: index%4==0
        if j % 4 == 0:
            bingo4 += 1

    print("index = ", index[i])
    print(bingo1, bingo2, int(bingo3/5), int(bingo4/5))
    print(bingo1 + bingo2 + int(bingo3/5) + int(bingo4/5))
    return bingo1 + bingo2 + int(bingo3/5) + int(bingo4/5)


myBingo = [list(map(int, input().split())) for _ in range(5)]
answer = [list(map(int, input().split())) for _ in range(5)]

# 숫자의 인덱스로 변환한 배열
index = [-1] * 25
for i in range(0, 5):
    for j in range(0, 5):
        index[i * 5 + j] = find_num(answer[i][j])
print(index)
for i in range(0, 25):
    if count_bingo(i) >= 3:
        print(index[i])
        break
