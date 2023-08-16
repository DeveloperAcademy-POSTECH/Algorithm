#백준-2559-수열
#https://www.acmicpc.net/problem/2559

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
temps = list(map(int, input().split()))

temp_value = sum(temps[0:k])
max_value = temp_value
for i in range(1, n-k+1):
    temp_value += temps[i+k-1] - temps[i-1]
    max_value = max(max_value, temp_value)
    
print(max_value)
