# https://www.acmicpc.net/problem/2565

import sys

input = sys.stdin.readline

n = int(input())
pair = []
max_num = 0
for _ in range(n):
    a, b = map(int, input().split())
    max_num = max(max_num, a)
    pair.append((a, b))
    
pair = sorted(pair)
dp = [0] * (501)
for i in range(len(pair)):
    a, b = pair[i]
    dp[a] += 1
    for j in range(i+1, len(pair)):
        if pair[j][1] > b:
            dp[pair[j][0]] = max(dp[pair[j][0]], dp[a])
           
print(n - max(dp))
