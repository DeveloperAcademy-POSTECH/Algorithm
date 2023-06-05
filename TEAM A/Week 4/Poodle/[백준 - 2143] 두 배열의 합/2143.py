# 백준 2143번: 두 배열의 합

from collections import defaultdict
import sys

input = sys.stdin.readline

# T <= 10^9
T = int(input())

# N <= 10^3
N = int(input())
A = list(map(int, input().rstrip().split()))

# M <= 10^3
M = int(input())
B = list(map(int, input().rstrip().split()))

# prefix sum을 각각 만든다면?

prefix_A = [0]
for a in A:
    prefix_A.append(prefix_A[-1] + a)

prefix_B = [0]
for b in B:
    prefix_B.append(prefix_B[-1] + b)

sub_A = []
for i in range(N):
    for j in range(i + 1, N + 1):
        sub_A.append(prefix_A[j] - prefix_A[i])

sub_B = []
for i in range(M):
    for j in range(i + 1, M + 1):
        sub_B.append(prefix_B[j] - prefix_B[i])

sub_A.sort()
sub_B.sort()

counter_B = defaultdict(int)
for b in sub_B:
    counter_B[b] += 1
sub_B = list(set(sub_B))

answer = 0

for a in sub_A:
    target = T - a
    left, right = 0, len(sub_B) - 1

    while left <= right:
        middle = (left + right) // 2

        if sub_B[middle] == target:
            answer += counter_B[sub_B[middle]]
            break
        elif sub_B[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

print(answer)
