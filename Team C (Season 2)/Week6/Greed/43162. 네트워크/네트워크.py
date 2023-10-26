from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n

    def bfs(start):
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            cur_v = queue.popleft()
            
            for i in range(n):
                if computers[cur_v][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

    for i in range(n):
        # 혼자 있어도 네트워크 1개로 치니까
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer
