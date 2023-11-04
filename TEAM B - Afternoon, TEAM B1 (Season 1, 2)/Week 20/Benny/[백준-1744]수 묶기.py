# https://www.acmicpc.net/problem/1744

import sys, heapq

input = sys.stdin.readline

n = int(input())
pos = []
other = []

for _ in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(pos, -num)
    elif num <= 0:
        heapq.heappush(other, num)
        
result = 0
while len(pos) > 1:
    first, second = -heapq.heappop(pos), -heapq.heappop(pos)
    result += max(first * second, first + second)

while len(other) > 1:
    first, second = heapq.heappop(other), heapq.heappop(other)
    result += first * second
    
result += -sum(pos) + sum(other)
print(result)