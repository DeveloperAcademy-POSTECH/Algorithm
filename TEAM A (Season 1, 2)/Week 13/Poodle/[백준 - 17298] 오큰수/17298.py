# 백준 17298번: 오큰수

import sys

input = sys.stdin.readline

# N <= 10^6
N = int(input())

arr = list(map(int, input().rstrip().split()))

# arr의 모든 수를 한 번 순회하는 것은 10^6
# 어떻게든 스택을 활용해야 함

# 관찰 키워드 1: 마지막은 무조건 -1
# 관찰 키워드 2: 역순?

# []        7   -1  [7]
# [7]       2   7   [7, 2]
# [7, 2]    5   7   [7, 5]
# [7, 5]    3   5   [7, 5, 3]

stack = []
answer = []

for idx in range(len(arr) - 1, -1, -1):
    current = arr[idx]

    while stack and stack[-1] <= current:
        stack.pop()
    right_biggest = stack[-1] if stack else -1

    stack.append(current)
    answer.append(right_biggest)

print(*answer[::-1])
