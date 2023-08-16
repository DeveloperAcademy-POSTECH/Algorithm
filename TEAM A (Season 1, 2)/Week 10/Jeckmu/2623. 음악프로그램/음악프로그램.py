from collections import deque
N, M = map(int, input().split())

graph_in_cnt = dict(zip([i for i in range(1, N+1)], [0 for _ in range(N)]))
graph_in = dict(zip([i for i in range(1, N+1)], [[] for _ in range(N)]))
graph_out = dict(zip([i for i in range(1, N+1)], [[] for _ in range(N)]))

for _ in range(M):
    a = list(map(int, input().split()))
    k = a[0]
    for i in range(1, k):
        graph_in_cnt[a[i+1]] += 1
        graph_in[a[i+1]].append(a[i])
        graph_out[a[i]].append(a[i+1])

queue = deque()
for i in graph_in_cnt:
    if graph_in_cnt[i] == 0:
        queue.append(i)

result = []
while queue:
    a = queue.popleft()

    for g in graph_out[a]:
        graph_in_cnt[g] -= 1
        if graph_in_cnt[g] == 0:
            queue.append(g)

    result.append(a)

# result에 N개의 원소가 없다면, 온전하게 종료되지 못한 것. exit.
if len(result) == N:
    for i in result:
        print(i)
else:
    print(0)