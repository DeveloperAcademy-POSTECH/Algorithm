import sys
sys.setrecursionlimit(10**5)

answer = False
N, M, X, Y, R, C, K = -1, -1, -1, -1, -1, -1, -1

# 사전식 우선순위로 정렬
moves = ((1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u'))

def dfs(r, c, depth, path):
    global answer
    global K, R, C
    
    # print(f"{r}, {c}, {depth}, {path}")
    
    if answer: return
    
    min_distance = abs(r - R) + abs(c - C)
    if K - depth < min_distance: return
    elif (K - depth - min_distance) % 2 == 1: return
    
    if depth == K:
        if r == R and c == C:
            answer = path
            print(answer)
        return
    
    for dr, dc, direction in moves:
        if 0 <= r + dr < N and 0 <= c + dc < M:
            dfs(r + dr, c + dc, depth + 1, path + direction)
    

def solution(n, m, x, y, r, c, k):
    global answer
    global N, M, X, Y, R, C, K
    
    N, M, X, Y, R, C, K = n, m, x - 1, y - 1, r - 1, c - 1, k
    
    min_distance = abs(X - R) + abs(Y - C)
    if k < min_distance: return "impossible"
    elif (k - min_distance) % 2 == 1: return "impossible"

    dfs(X, Y, 0, "")
    
    # print(answer)
    
    return answer
