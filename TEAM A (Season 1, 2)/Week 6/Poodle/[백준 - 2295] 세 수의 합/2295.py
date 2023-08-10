# 백준 2295번: 세 수의 합

import sys

input = sys.stdin.readline

# N <= 10^3
N = int(input())

numbers = [int(input()) for _ in range(N)]
numbers.sort()

two_sums = set()

for x in numbers:
    for y in numbers:
        two_sums.add(x + y)

two_sums = list(two_sums)
two_sums.sort()

answer = 0

for z in numbers:
    for k in numbers:
        target = abs(k - z)

        left, right = 0, len(two_sums) - 1

        while left <= right:
            middle = (left + right) // 2

            if two_sums[middle] == target:
                answer = max(answer, max(k, z))
                break
            elif two_sums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

print(answer)
