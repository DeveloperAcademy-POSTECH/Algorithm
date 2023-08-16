import sys
sys.setrecursionlimit(100000)
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [0]*26
maxDepth = 0


def dfs(i, j, depth):
    global maxDepth
    if maxDepth < depth:
        maxDepth = depth

    for k in range(4):
        di = i + dy[k]
        dj = j + dx[k]
        if 0 <= di < R and 0 <= dj < C and visited[ord(board[di][dj])-65] != 1:
            visited[ord(board[di][dj])-65] = 1
            dfs(di, dj, depth+1)
            visited[ord(board[di][dj])-65] = 0


visited[ord(board[0][0])-65] = 1
dfs(0, 0, 1)

print(maxDepth)
