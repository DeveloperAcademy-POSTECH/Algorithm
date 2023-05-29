# N 은 100만개
# 무조건 nLogn 정도로 풀어야함
# 
# N개의 좌표에 좌표압축을 적용
# Xi 를 압축한 결과 X'i 의 값은
# Xi > Xj 를 만족하는 서로 다른 좌표의 개수와 같아야 한다? 뭔 소리여 이게
# X'1 의 값은 X1 > Xj 를 만족하는 서로 다른 좌표의 갯수와 같아야한다.
# 아 전체 list 에서 해당 좌표보다 작은 숫자를 쓰는거구나

# 그렇다면 일단 각 좌표를 dict 로 만들고, list 를 돌면서 해당 좌표보다 작은지 항상 체크해야할듯?
# 근데 이러면 n^2 아닌가..?
# 한번 sort 하고, dict 로 돈다면? 
# 아니면 한번 sort 하고, 각 index 를 연산해서 숫자를 구한다면?

import sys
sys.stdin = open("18870_compress_coordinates/compress_coordinates.txt", "r")

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))
cpy_num_list = sorted(num_list[:])
print(cpy_num_list)