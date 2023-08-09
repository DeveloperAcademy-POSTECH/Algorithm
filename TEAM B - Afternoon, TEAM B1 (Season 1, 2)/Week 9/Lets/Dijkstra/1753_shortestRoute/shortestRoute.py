# 백준 1753
# https://www.acmicpc.net/problem/1753


# 방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램

# 정점 갯수 V <= 20,000, 간선 갯수 E <= 300,000)
# 모든 정점에는 1부터 번호가 있음
# 간선에는 가중치가 존재
# 서로 다른 두 정점 사이에 여러개의 간선이 존재할 수 있음


# 입력
# (u, v, w)

# 출력
# i 번 정점으로의 최단 경로의 경로값을 출력.
# 경로가 존재하지 않는 경우 INF 출력


# 1초, 기본 다익스트라는 O(V^2) 니까 4000000000 이면 40억이네...

# heap 을 써야겠구만
# 근데 heap 으로 어떻게 구현하지?
# 근데 heap 안에 있는것들의 값을 바꿔도 자동으로 heap 이 재정렬되나?
# -> 이렇게 하는게 아니라 업데이트 될때마다 업데이트 내역을 heap 에 넣음, 만약 겹치는게 있다면 현재보다 안좋다면 무시
import sys
import heapq
sys.stdin = open("1753_shortestRoute/shortestRoute.txt", "r")

V, E = list(map(int, sys.stdin.readline().split()))

start = int(sys.stdin.readline())

# 간선 처리용 dict
edgeDict = {}


for _ in range(E):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    if edgeDict.get(u):
        edgeDict[u].append((v, w))
    else:
        edgeDict[u] = [(v, w)]

# 엄청 큰 값을 나타내는
INF = int(1e9)

# 최소거리들을 나타내는 용
distance = [INF for _ in range(V+1)]
distance[start] = 0

# 우선순위 큐
heap = [(0, start)]

def updateDistance(start, vertex, weight):
    newDistance = distance[start] + weight
    if distance[vertex] > newDistance: # 만약 새로운 최소거리라면
        distance[vertex] = newDistance # 업데이트를 해주고
        heapq.heappush(heap, (newDistance, vertex))

# 우선순위큐를 이용한 개선된 다익스트라
def advancedDijkstra():
    while heap:
        # 최소거리인 노드 뽑기
        accumulatedDistance, start = heapq.heappop(heap)

        # 만약 현재 뽑은 노드의 최소거리보다 길다? -> 무시
        if accumulatedDistance > distance[start]:
            continue

        # 해당 node 와 연결된 node 들 확인
        connections = edgeDict.get(start)
        if connections == None:
            continue

        # 업데이트 진행
        for i in range(len(connections)):
            vertex, weight = connections[i]
            updateDistance(start, vertex, weight)


advancedDijkstra()

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])        

# dictinary 를 이용해서 간선 갯수를 줄이면 어떨까?
# import sys
# sys.stdin = open("1753_shortestRoute/shortestRoute.txt", "r")
# sys.setrecursionlimit(10**8)

# V, E = list(map(int, sys.stdin.readline().split()))

# start = int(sys.stdin.readline())

# # 2차원 배열이 아닌 dict 로 간선표현
# edgeDict = {}
# for _ in range(E):
#     u, v, w = list(map(int, sys.stdin.readline().split()))
#     if edgeDict.get(u):
#         edgeDict[u].append((v, w))
#     else:
#         edgeDict[u] = [(v, w)]

# # 방문처리용
# visited = [False for _ in range(V+1)]
# visited[0], visited[start] = True, True

# # 축적거리용
# INF = V * V * E
# distance = [INF for _ in range(V+1)]
# distance[0], distance[start] = 0, 0 # distance[0] 을 0 처리해도 되는 이유? -> 어짜피 visited 도 True 처리를 해놔서 걸러짐

# # 다음 최소 축적거리 노드를 뽑아내는 함수
# def getNextNode():
#     maxValue = INF
#     index = -1

#     for i in range(V+1):
#         if not visited[i] and distance[i] < maxValue:
#             index, maxValue = i, distance[i]
    
#     return index

# # 돌떄마다 축적거리를 업데이트 하는 함수
# def updateNode(start, target, weight):
#     distance[target] = min(distance[target], distance[start]+weight)


# # 다익스트라
# def dijkstra(start):
#     # 방문처리
#     visited[start] = True

#     # 본인과 연결된 node 들을 파악
#     connectedInfo = edgeDict.get(start)
#     if connectedInfo == None:
#         return

#     # 연결된 노드들을 순환하면서 업데이트
#     for i in range(len(connectedInfo)):
#         target, weight = connectedInfo[i]

#         updateNode(start, target, weight)

#     # 업데이트가 끝났다면? -> 다음번 노드를 찾는다
#     nextNode = getNextNode()
#     if nextNode == -1:
#         return
    
#     # 다음번 node 에서 dijkstra 진행
#     dijkstra(nextNode)

# dijkstra(start)

# for i in range(1, V+1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])

### 일단은 기본 풀이
# 일단 기본 다익스트라를 내 손으로 구현해보자. 그리고 시간초과 나는걸 보고 향상된 다익스트라로 바꾸자

# import sys
# sys.stdin = open("1753_shortestRoute/shortestRoute.txt", "r")

# V, E = list(map(int, sys.stdin.readline().split()))
# start = int(sys.stdin.readline())
# # start = 1

# INF = V * E

# # 간선에 대한 정보 구현
# connections = [[0 for _ in range(V+1)] for _ in range(V+1)]

# # 간선 정보 받기
# for _ in range(E):
#     u, v, w = list(map(int, sys.stdin.readline().split()))
#     connections[u][v] = w
#     # connections[v][u] = w

# # 각 노드에 대한 방문처리용
# visited = [False for _ in range(V+1)]
# visited[0], visited[start] = True, True

# # 각 노드까지의 최소거리를 나타내는 리스트
# distance = [INF for _ in range(V+1)]
# distance[0], distance[start] = 0, 0



# # 매번마다 누적값이 최소인 node 를 뽑아내는 함수
# def getNextNode():
#     maxValue = INF
#     index = -1

#     for i in range(V+1):
#         if not visited[i] and distance[i] < maxValue:
#                 index, maxValue = i, distance[i]
    
#     return index


# def dijkstra(start):
#     visited[start] = True
#      # 현재 노드에서 갈 수 있는 노드들을 찾는다
#     for i in range(V+1):
#         if connections[start][i] != 0: # 연결이 있는 노드를 찾았다면
#              # 그 노드의 축적값을 갱신한다.
#             distance[i] = min(distance[i], distance[start]+connections[start][i])

#     nextNode = getNextNode()

#     if nextNode == -1:
#          return
    
    
#     dijkstra(nextNode)

# dijkstra(start)


# for i in range(1, V+1):
#     if distance[i] != INF:
#         print(distance[i])
#     else:
#         print("INF")
