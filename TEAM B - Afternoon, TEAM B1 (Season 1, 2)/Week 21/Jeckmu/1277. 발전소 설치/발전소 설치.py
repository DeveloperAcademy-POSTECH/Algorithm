from math import sqrt
import heapq

N, W = map(int, input().split())
M = float(input())

v = []
for _ in range(N):
    v.append(list(map(int, input().split())))

def distance(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)
    
# graph 초기화
graph = [[1e9]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i==j: continue
        graph[i][j] = distance(v[i][0], v[i][1], v[j][0], v[j][1])
        # M보다 거리가 멀면, max값을 넣음.
        if graph[i][j] > M:
            graph[i][j] = 1e9

# 이미 연결된 전선의 cost(거리)는 0으로
for _ in range(W):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 0
    graph[b-1][a-1] = 0

# 다익스트라    
distance = [1e9]*N
distance[0] = 0

q = []
heapq.heappush(q, (0, 0))   # 0번 node(1번) 부터 start. cost는 0.

while q:
    dist, node = heapq.heappop(q)
    
    # visited 확인
    if distance[node] < dist:
        continue
    
    for i, cost in enumerate(graph[node]):
        if cost == 1e9:    # M보다 큰 거리 or i==j
            continue
        
        newCost = dist + cost
        if newCost < distance[i]:
            distance[i] = newCost
            heapq.heappush(q, (newCost, i))
            
print(int(distance[N-1]*1000))