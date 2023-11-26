import sys
sys.setrecursionlimit(int(1e5))

T = int(input())

for _ in range(T):
    N = int(input())
    parent = [0] * (N+1)
    depth = [0] * (N+1)
    cal = [False] * (N+1)
    tree = [[] for _ in range(N + 1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
        parent[b] = a

    # 루트 노드 찾기 (parent가 0(초기값)이면 root)
    root = 0
    for i in range(1, N+1):
        if parent[i] == 0:
            root = i
            
    # 루트 노드부터 depth 저장.
    def dfs(x, dep):
        cal[x] = True
        depth[x] = dep
        for y in tree[x]:
            if cal[y]:
                continue
            parent[y] = x
            dfs(y, dep+1)
    
    # Lowest Common Ancestor
    def LCA(x, y):
        while depth[x] != depth[y]:
            if depth[x] > depth[y]:
                x = parent[x]
            else:
                y = parent[y]
        
        while x != y:
            x = parent[x]
            y = parent[y]
        
        return x

    # root부터 dfs를 통해 depth 저장
    dfs(root, 0)
    
    # LCA
    n, m = map(int, input().split())
    print(LCA(n, m))