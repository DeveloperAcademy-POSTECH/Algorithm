N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(1 << N)] for _ in range(N)]


def dfs(row, visit, start, cnt):
    if cnt == N:
        return 0

    if visited[row][visit] != -1:
        return visited[row][visit]

    ret = 10000000
    for i in range(N):
        if visit & (1 << i) != 0 or city[row][i] == 0:
            continue
        if (cnt == N - 1 and i != start) or (cnt != N - 1 and i == start):
            continue

        ret = min(ret, dfs(i, visit | (1 << i), start, cnt + 1) + city[row][i])

    visited[row][visit] = ret

    return visited[row][visit]


print(dfs(0, 0, 0, 0))