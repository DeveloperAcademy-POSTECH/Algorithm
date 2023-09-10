# 백준 2623번: 음악프로그램

from collections import deque, defaultdict
import sys

input = sys.stdin.readline

# N <= 10^3, M <= 10^2
N, M = map(int, input().rstrip().split())

childs = defaultdict(list)
num_parents = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    _, *orders = list(map(int, input().rstrip().split()))

    for idx in range(len(orders) - 1):
        parent = orders[idx]

        for child in orders[idx + 1:]:
            childs[parent].append(child)
            num_parents[child] += 1
# print(childs)

q = deque()
for idx in range(1, N + 1):
    if num_parents[idx] == 0:
        q.append(idx)
        visited[idx] = True
# print(q, num_parents[1:])

answer = []
wrong = False

while q:
    current = q.popleft()
    # print("current:", current)
    answer.append(current)

    for child in childs[current]:
        num_parents[child] -= 1

        if num_parents[child] == 0:
            if not visited[child]:
                q.append(child)
            else:
                wrong = True
                break
    if wrong: break
    # print(q, num_parents[1:])

if len(answer) != N: print(0)
else:
    for ans in answer:
        print(ans)
