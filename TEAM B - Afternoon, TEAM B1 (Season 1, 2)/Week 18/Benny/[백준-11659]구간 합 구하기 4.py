# https://www.acmicpc.net/problem/11659

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
accumulated = [0]
for i in range(len(nums)):
    accumulated.append(accumulated[i] + nums[i])
    
for _ in range(m):
    i, j = map(int, input().split())
    print(accumulated[j] - accumulated[i-1])

    

