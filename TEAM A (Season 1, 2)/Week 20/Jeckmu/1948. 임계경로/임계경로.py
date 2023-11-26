from collections import deque
n = int(input())
m = int(input())

# Topological Sort Setting & Time
graph_in_cnt = [0 for _ in range(n+1)]
graph_in = [[] for _ in range(n+1)]
graph_out = [[] for _ in range(n+1)]

# Input
for _ in range(m):
    a, b, t = map(int, input().split())
    graph_in[b].append((a, t))
    graph_out[a].append((b, t))
    graph_in_cnt[b] += 1
    
start, end = map(int, input().split())

# 도시별 최대 시간
max_time = [0]*(n+1)

# Topological Sort
deq = deque([start])
while deq:
    s = deq.popleft()
    
    for e, t in graph_out[s]:
        graph_in_cnt[e] -= 1
        # 도시별 최대 도달 시간 갱신
        max_time[e] = max(max_time[e], max_time[s] + t)
        if graph_in_cnt[e] == 0:
            deq.append(e)

# 목적지에서의 최대 도달 시간은 도시마다의 최대 도달 시간으로만 구성해도 구할 수 있다!
print(max_time[end])

# BackTracking
result = 0
visited = [False for _ in range(n+1)]
deq = deque([end])
while deq:
    e = deq.popleft()
    
    # 거꾸로 되돌아가면서, 지금 보는 경로가 s -> e일 때,
    # (e에서의 최대 도달 시간) - (s -> e 경로에 걸리는 시간) = (s에서의 최대 도달 시간) 이라면,
    # (그러니까, max_time[e] - time[s][e] == max_time[s] 라면,)
    # 카운팅할 경로에 추가! (최대 시간이 걸리는 경로임!)
    for s, t in graph_in[e]:
        if max_time[e] - t == max_time[s]:
            result += 1
            
            # 중복 제거
            if not visited[s]:
                deq.append(s)
                visited[s] = True

print(result)