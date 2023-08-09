# https://www.acmicpc.net/problem/1932
# 백준-1932-정수 삼각형

import sys

input = sys.stdin.readline

n = int(input())
integers = []
for _ in range(n):
    integers.append(list(map(int, input().split())))
    
for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            integers[i][j] += integers[i-1][0]
        elif j == i:
            integers[i][j] += integers[i-1][i-1]
        else:
            integers[i][j] += max(integers[i-1][j-1], integers[i-1][j])
            
print(max(integers[-1]))