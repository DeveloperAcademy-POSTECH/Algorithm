import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정.

# 노드, 간선 개수 입력
n, m = map(int, input().split())
# 시작노드 번호 입력.
start = int(input())

# 노드번호가 1~n 이기 때문에, 모든 리스트의 범위는 range(n+1)로 한다.

# graph : 각 노드에 연결되어 있는 노드의 정보를 담는 리스트 
graph = [[] for i in range(n+1)] 
    # 각 인덱스의 배열에 (목적지 노드, 거리)의 튜플을 append 예정.

# visited = 방문한 적이 있는지 체크하는 목적의 리스트 
visited = [False] * (n+1)

# distance : 최단거리 테이블, 모든 값을 무한으로 초기화.
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기. => a 노드에서 b노드로 가는 거리가 c
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환하는 함수.
# 다음에 방문할 노드를 고르기 위한.
def get_smaller_node():
    min_value = INF
    index = 0 # 가장 최단거리가 짧은 노드
    for i in range(1, n+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return index

def dijkstra(start) :
# 시작노드에 대한 초기조건 
    distance[start] = 0
    visited[start] = True
    # 1번 노드와 각 노드들의 거리를, 각 노드의 distance table에 업데이트.
    for j in graph[start] :
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의노드에 대해 반복.
    for i in range(n-1): # now 노드가 무엇이든 결국 모든 나머지 노드가 한번씩은 now가 되기 때문에 (탐색 순서의 문제)
        now = get_smaller_node()
        visited[now] = True
        # ⭐️ 현재 노드와 연결된 다른 노드 확인. (-> 거쳐가는)
        for k in graph[now]: #이 now 노드와 연결된 다른 노드들에 대해
            cost = distance[now] + k[i] 
            #cost와 distance의 값을 비교해, 더 작은 것으로 업데이트
            if cost < distance[k[0]] :
                distance[k[0]] = cost

# 다익스트라 알고리즘의 수행
dijkstra(start)

# 최단거리의 출력 => distance 테이블의 출력

for i in range(1, n+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])