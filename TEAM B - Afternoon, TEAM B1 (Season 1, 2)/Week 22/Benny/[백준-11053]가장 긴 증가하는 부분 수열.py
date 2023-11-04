# https://www.acmicpc.net/problem/11053
# 백준-11053-가장 긴 증가하는 부분 수열

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums = [0] + nums
dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(0, i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))