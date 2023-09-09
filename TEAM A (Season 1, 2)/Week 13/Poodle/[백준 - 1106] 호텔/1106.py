# 백준 1106번: 호텔 풀이

import sys

input = sys.stdin.readline

# C <= 10^3, N <= 20
C, N = map(int, input().rstrip().split())

costs = [0]
customers = [0]

for _ in range(N):
    cost, customer = map(int, input().rstrip().split())

    costs.append(cost)
    customers.append(customer)

# dp[i][w]: 1번째 ~ i번째 도시까지 고려했을 때, 적어도 고객 w명을 홍보할 수 있는 최소 비용
dp = [[int(1e9) for _ in range(C + 1)] for _ in range(N + 1)]

# for row in dp:
#     print(row)
# print()

for i in range(1, N + 1):
    cost = costs[i]
    customer = customers[i]

    for w in range(1, C + 1):
        dp[i][w] = dp[i - 1][w]

        k = 0
        while True:
            # 최소 고객을 맞추기 위한 이번 도시의 최소 투자 비용이 결정되면
            if w <= k * customer:
                # 기존 값과 비교해서 갱신
                dp[i][w] = min(dp[i][w], k * cost)
                break
            else:
                dp[i][w] = min(dp[i][w], dp[i - 1][w - k * customer] + k * cost)
            
            k += 1
        
    # for row in dp:
    #     print(row)
    # print()

print(dp[N][C])
