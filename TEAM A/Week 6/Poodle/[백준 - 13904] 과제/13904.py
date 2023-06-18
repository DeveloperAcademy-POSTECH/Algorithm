# 백준 13904번: 과제

import sys
import heapq

input = sys.stdin.readline

# N <= 10^3
N = int(input())

homeworks = []

for _ in range(N):
    # D <= 10^3, W <= 10^2
    D, W = map(int, input().rstrip().split())

    heapq.heappush(homeworks, (N - D, W))

answer = 0
current = []

# 마감일부터 거꾸로 계산해오며 할 수 있는 과제들의 리스트 접근
for day in range(N):
    # 1. 현재 날 수 기준 할 수 있는 모든 과제들을 current에 추가
    while homeworks:
        temp_day, temp_score = heapq.heappop(homeworks)

        if day >= temp_day:
            current.append(temp_score)
        else:
            heapq.heappush(homeworks, (temp_day, temp_score))
            break

    # print(current)

    # 2. 할 수 있는 과제들 리스트 중 하나를 빼서 answer에 추가
    if len(current) > 0:
        answer += max(current)
        current.remove(max(current))

    # print(answer)
    # print()

print(answer)
