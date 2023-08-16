from collections import deque
N, M = map(int, input().split())

graph_in_cnt = dict(zip([i for i in range(1, N+1)], [0 for _ in range(N)]))
graph_in = dict(zip([i for i in range(1, N+1)], [[] for _ in range(N)]))
graph_out = dict(zip([i for i in range(1, N+1)], [[] for _ in range(N)]))

for i in range(M):
    a, b = map(int, input().split())
    graph_in_cnt[b] += 1
    graph_in[b].append(a)
    graph_out[a].append(b)

queue = deque()
for g in graph_in_cnt:
    if graph_in_cnt[g] == 0:
        queue.append(g)

result = []
while queue:
    a = queue.popleft()
    result.append(a)

    for k in graph_out[a]:
        graph_in_cnt[k] -= 1
        if graph_in_cnt[k] == 0:
            queue.append(k)

print(*result)