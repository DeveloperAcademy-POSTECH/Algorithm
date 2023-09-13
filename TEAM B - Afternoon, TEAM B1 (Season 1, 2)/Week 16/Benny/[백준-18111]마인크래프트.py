# https://www.acmicpc.net/problem/18111
# 백준-18111-마인크래프트

import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
heights = []
for _ in range(n):
    heights.append(list(map(int, input().split())))
    
INF = 999999999
solution = [INF, 0]
for level in range(256, -1, -1):
    push_count = 0
    pop_count = 0
    for i in range(n):
        for j in range(m):
            if heights[i][j] >= level:
                pop_count += heights[i][j] - level
            else:
                push_count += level - heights[i][j]
    if b + pop_count - push_count >= 0:
        sec = 2 * pop_count + push_count
        if sec < solution[0]:
            solution = [sec, level]
        
print(' '.join(map(str, solution)))