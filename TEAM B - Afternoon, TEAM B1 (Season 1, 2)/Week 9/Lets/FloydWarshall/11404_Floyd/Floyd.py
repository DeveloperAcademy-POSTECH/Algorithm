# 백준 11404: 플로이드
# https://www.acmicpc.net/problem/11404
# n <= 100, m <= 100,000

# 모든 도시 쌍에 대해서 필요한 비용의 최솟값은?
# -> 플로이드 와샬

# 시작도시와 도착도시를 연결하는 노선은 하나가 아닐 수 있다.
# 시작도시 a, 도착도시 b, 비용 c
# 근데 이거 방향성이 있는 그래프인가?

import sys
sys.stdin = open("11404_Floyd/Floyd.txt")

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(1e9)
connections = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, weight = list(map(int, sys.stdin.readline().split()))
    connections[start][end] = min(connections[start][end], weight)

for i in range(n+1):
    connections[i][i] = 0

# 각 노드에 대해, 해당 노드를 거쳐서 갈 수 있는 곳들에 대한 순서쌍들을 구함
for standardNode in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i == j: # 자기 자신으로 오는것은 제외
                continue

            connections[i][j] = min(connections[i][j], connections[i][standardNode] + connections[standardNode][j])
    
for i in range(1, n+1):
    line = ""
    for j in range(1, n+1):
        if connections[i][j] == INF:
            line += "0 "
        else:
            line += f"{connections[i][j]} "
    print(line)
