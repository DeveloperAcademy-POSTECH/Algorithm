# 백준 2252번: 줄 세우기

from collections import deque, defaultdict
import sys

input = sys.stdin.readline

# N < 4 * 10^4, M <= 10^5
N, M = map(int, input().rstrip().split())

# 위상 정렬을 위한 후행 작업 노드 및 선행 작업 수 리스트 초기화
childs = defaultdict(list)
number_parents = [0 for _ in range(N + 1)]

answer = []

for _ in range(M):
    A, B = map(int, input().rstrip().split())

    # A -> B의 정렬 순서가 보장되어야 함
    childs[A].append(B)
    number_parents[B] += 1

# 앞에 서야 하는 학생 수가 0인 노드들을 큐에 넣기
q = deque([])
for idx in range(1, N + 1):
    if number_parents[idx] == 0:
        q.append(idx)

while q:
    # 큐에서 1개씩 뽑기
    current = q.popleft()
    answer.append(current)

    # 연결된 간선 끊기
    for child in childs[current]:
        number_parents[child] -= 1

        # 앞에 서야 하는 학생 수가 0인 노드들을 큐에 넣기
        if number_parents[child] == 0:
            q.append(child)

print(*answer)
