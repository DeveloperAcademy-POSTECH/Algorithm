import sys
sys.setrecursionlimit(10**6)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    def dfs(x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if graph[y][x] == 1:
            graph[y][x] = 0
            dfs(x, y - 1)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x + 1, y)
            return True
        return False

    count = 0
    for y in range(n):
        for x in range(m):
            if dfs(x, y) == True:
                count += 1

    print(count)