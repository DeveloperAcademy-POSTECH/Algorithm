# https://www.acmicpc.net/problem/12865
# 백준-12865-평범한 배낭

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

stuffs = [[0, 0]]
for _ in range(n):
    stuffs.append(list(map(int, input().split())))
    
max_values = [[0]*(k+1)]
for i in range(1, n+1):
    temp = []
    for j in range(k+1):
        if stuffs[i][0] > j:
            temp.append(max_values[i-1][j])
        else:
            temp.append(max(max_values[i-1][j-stuffs[i][0]]+stuffs[i][1], max_values[i-1][j]))
    max_values.append(temp)

print(max_values[-1][-1])