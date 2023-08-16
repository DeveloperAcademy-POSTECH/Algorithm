import heapq
N = int(input())

assignments = []
for _ in range(N):
    a = tuple(map(int, input().split()))
    a = (-a[1], a[0])    # reverse tuple (for append in Priority Queue(heapq))
    heapq.heappush(assignments, a)

result = {}
while assignments:
    a = heapq.heappop(assignments)

    day = a[1]
    while True:
        if day == 0:
            break

        if result.get(day):
            day -= 1
            continue
        else:
            result[day] = -a[0]
            break

print(sum(result.values()))