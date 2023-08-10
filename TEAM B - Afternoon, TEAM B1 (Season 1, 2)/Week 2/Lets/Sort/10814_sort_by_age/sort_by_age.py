# N 은 100,000 - > Nlog(N) 정도로 풀자
# 사람의 나이, 이름이 가입한 순서대로 주어짐
# 나이순으로 정렬하고, 나이가 같으면 가입한 순서대로 정렬
# 가입한 순서대로 정렬한번 하고, stable 하게 나이순으로 정렬하면 되지 않을까?
# -> python 의 sort 는 stable 이라서 이게 되네... 굿

import sys
sys.stdin = open("10814_sort_by_age/sort_by_age.txt", "r")

N = int(sys.stdin.readline())

info = []
for i in range(N):
    age, name = list(sys.stdin.readline().split())
    age = int(age)
    info.append([age, name, i])



info.sort(key = lambda x: x[2]) # 가입한 순서대로 한번 정렬
info.sort(key = lambda x: x[0]) # 나이순으로 정렬

for item in info:
    print(f"{item[0]} {item[1]}")