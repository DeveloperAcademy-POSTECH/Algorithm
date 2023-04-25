import sys

input = sys.stdin.readline

# R, C <= 2 * 10
R, C = map(int, input().rstrip().split())

board = [list(input().rstrip()) for _ in range(R)]

# for row in board:
#     print(row)

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
answer = -1

# 1. (0, 0)부터 탐색하기 시작
# 2. BFS는 큐의 크기가 너무 커질 것을 염려해, DFS로 접근해 보기로 함
# 3. 이전에 지나온 칸들을 기록하고 있어야 함 -> set()
# -> 이렇게만 할 시에 22% 쯤에서 시간 초과 남

# 4. set 쓰면 시간 초과, 문자열 쓰면 통과함
# 5. 안 해보긴 했지만 BFS로 풀었으면 메모리 초과 났을 것

def dfs(r, c, visited, level):
    # print(f"({r}, {c})")

    global answer
    answer = level if answer < level else answer
    # print(answer)

    for dr, dc in moves:
        if 0 <= r + dr < R and 0 <= c + dc < C:
            if board[r + dr][c + dc] not in visited:
                dfs(r + dr, c + dc, visited + board[r + dr][c + dc], level + 1)

dfs(0, 0, board[0][0], 1)
print(answer)
