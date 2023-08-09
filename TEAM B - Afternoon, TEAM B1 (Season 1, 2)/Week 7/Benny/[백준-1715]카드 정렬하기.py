# https://www.acmicpc.net/problem/1715
# 백준-1715-카드 정렬하기

import sys, heapq

n = int(sys.stdin.readline())
answer = 0
h = []
for _ in range(n):
    heapq.heappush(h, int(sys.stdin.readline()))
    
while len(h) > 1:
    temp = heapq.heappop(h) + heapq.heappop(h)
    heapq.heappush(h, temp)
    answer += temp

print(answer)
    