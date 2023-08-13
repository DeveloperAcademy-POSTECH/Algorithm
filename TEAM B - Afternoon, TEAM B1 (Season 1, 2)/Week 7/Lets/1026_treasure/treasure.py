# 백준 1026: 보물
# https://www.acmicpc.net/problem/1026

# 함수 s 는 정수 배열 A 와 B 의 index 가 같은 걸 곱한것의 합
# S 의 값을 가장 작게 만들기 위해 A 를 재배열, B 는 재배열 x

# N < 50, 2초 -> 그렇다면 연산이 엄청 많다는거 아닌가?
# -> ?? 아니네.. 뭐여 이문제

# A 가 재배열 가능하면 B 의 재배열 가능 불가능 여부는 상관없고
# 큰값 * 큰값 하면 너무 큰 값되니까 가장 작은값 * 가장 큰 값 을 계속 해나감

import sys


sys.stdin = open("1026_treasure/treasure.txt", "r")

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

total = 0
for i in range(N):
    total += A[i] * B[i]

print(total)