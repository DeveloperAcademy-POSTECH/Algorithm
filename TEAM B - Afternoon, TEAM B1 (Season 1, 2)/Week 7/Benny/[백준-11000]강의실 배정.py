import sys, heapq

input = sys.stdin.readline

n = int(input())
classes = []
ends = []

for _ in range(n):
    start, end = map(int, input().split())
    heapq.heappush(classes, (start, end))

start, end = heapq.heappop(classes)
heapq.heappush(ends, end)
while classes:
    start, end = heapq.heappop(classes)
    if start >= ends[0]:
        heapq.heappop(ends)
        heapq.heappush(ends, end)
    else:
        heapq.heappush(ends, end)
    
print(len(ends))