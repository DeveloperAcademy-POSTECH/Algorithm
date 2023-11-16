N, M = map(int, input().split())

graph = {}
for _ in range(M):
    a, b = map(int, input().split())
    if graph.get(a):
        graph[a].append(b)
    else:
        graph[a] = [b]

    if graph.get(b):
        graph[b].append(a)
    else:
        graph[b] = [a]

result = 10e9
for A in range(1, N+1):
    if not graph.get(A):
        continue
    for B in graph[A]:
        # A - B 는 연결되어 있으므로, graph[A]에 B가 있다면,
        # graph[B]에도 A가 항상 존재한다. 따라서 아래 과정을 거칠 필요가 없다.
        ## if A not in graph[B]:
        ##    continue
        for C in graph[A]:
            if C == B:
                continue
            # 이 조건만 통과하면, A-B-C가 모두 친구인 것.
            if C in graph[B]:
                result = min(result, len(graph[A])+len(graph[B])+len(graph[C])-6)
                
if result == 10e9:
    print(-1)
else:
    print(result)