#https://www.acmicpc.net/problem/10165
#백준-10165-버스 노선

import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
routes = []
for i in range(m):
    a, b = map(int, input().split())
    if a < b:
        heapq.heappush(routes, (a, b, i))
        heapq.heappush(routes, (a+n, b+n, i))
    else:
        heapq.heappush(routes, (a, b+n, i))
        
is_included = [False] * m
a1, b1, i1 = heapq.heappop(routes)
while routes:
    a2, b2, i2 = heapq.heappop(routes)
    if a1 == a2:
        is_included[i1] = True
        b1, i1 = b2, i2
    elif b1 >= b2:
        is_included[i2] = True
    else:
        a1, b1, i1 = a2, b2, i2
        
print(' '.join(map(str, [i+1 for i in range(len(is_included)) if is_included[i] == False])))