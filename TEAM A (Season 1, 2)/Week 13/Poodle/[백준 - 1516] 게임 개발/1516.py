# 백준 1516번: 게임 개발

from collections import deque
import sys

input = sys.stdin.readline

# N <= 5 * 10^2
N = int(input())

# 뭔가 느낌은 위상 정렬 + 그리디

times = [0]
nexts = [[] for _ in range(N + 1)]
prevs = [0 for _ in range(N + 1)]

for idx in range(1, N + 1):
    T, *pre, _ = map(int, input().rstrip().split())
    times.append(T)
    
    for p in pre:
        nexts[p].append(idx)
        prevs[idx] += 1

# dp[idx]: idx번째 건물을 짓는 데 걸리는 총 소요 시간
dp = [0 for _ in range(N + 1)]

q = deque()

for idx in range(1, N + 1):
    if prevs[idx] == 0:
        q.append(idx)
        dp[idx] = times[idx]

while q:
    current = q.popleft()

    for next in nexts[current]:
        dp[next] = max(dp[next], dp[current] + times[next])

        prevs[next] -= 1
        if prevs[next] == 0:
            q.append(next)

for ans in dp[1:]:
    print(ans)
