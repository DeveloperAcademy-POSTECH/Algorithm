#https://www.acmicpc.net/problem/2579
# 백준-2579-계단 오르기

import sys

input = sys.stdin.readline

n = int(input())

steps = []
for _ in range(n):
    steps.append([int(input())]*2)
    
if n == 1:
    print(steps[0][0])
    
elif n == 2:
    print(steps[0][0] + steps[1][0])
    
else:
    steps[1][1] += steps[0][0]
    for i in range(2, len(steps)):
        steps[i][0] += max(steps[i-2][0], steps[i-2][1])
        steps[i][1] += steps[i-1][0]

    print(max(steps[-1][0], steps[-1][1]))