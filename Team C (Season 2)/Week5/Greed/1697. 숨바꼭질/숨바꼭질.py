from collections import deque
subin, sister = map(int, input().split())

def bfs(startV, goal):
    max_num = 100001
    visited = [False]*max_num
    queue = deque()
    queue.append(startV)
    visited[startV] = True

    while queue:
        cur_x = queue.popleft()

        if cur_x == goal:
            return visited[cur_x] - 1

        for next_x in (cur_x - 1, cur_x + 1, cur_x * 2):
            if next_x in range(max_num) and not visited[next_x]:
                queue.append(next_x)
                visited[next_x] = visited[cur_x] + 1

print(bfs(subin,sister))
