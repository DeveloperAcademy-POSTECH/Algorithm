# 백준 11047: 동전 0
# https://www.acmicpc.net/problem/11047

# 여러개의 코인을 더해서 특정 가격 맞추기
# 코인의 갯수 최소화하기
# 그렇다면 큰 값부터 넣어서 동전의 갯수 최소화

# A1 = 1 이니까 잔액이 남는 경우도 안존재함

# N < 10, K < 100,000,000

import sys
sys.stdin = open("11047_coin0/coin0.txt", "r")

N, K = map(int, sys.stdin.readline().split())


coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)

cnt = 0
for coin in coins:
    cnt += K // coin
    K %= coin

print(cnt)

