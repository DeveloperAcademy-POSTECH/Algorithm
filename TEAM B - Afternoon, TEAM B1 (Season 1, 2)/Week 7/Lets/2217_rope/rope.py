# 백준 2217: 로프
# https://www.acmicpc.net/problem/2217

# 2초, N <= 100,000

# k 개의 로프를 사용하면 w 인 물체를 들어올릴 때, 각각의 로프에 모두 w/k 의 중량이 걸림

# 이 로프들을 이용해서 들어올릴 수 있는 물체의 최대중량은?
# 임의의 몇개의 로프를 골라서 써도 되는구나
# 그러면 가장 약한 밧줄을 빼가면서 max 값을 비교해봐야겠다
# ->min heap


import sys
import heapq

sys.stdin = open("2217_rope/rope.txt", "r")

N = int(sys.stdin.readline())


ropes = []

for _ in range(N):
    heapq.heappush(ropes, int(sys.stdin.readline()))

max_weight = 0
while ropes:
    max_weight = max(max_weight, len(ropes)*heapq.heappop(ropes))

print(max_weight)