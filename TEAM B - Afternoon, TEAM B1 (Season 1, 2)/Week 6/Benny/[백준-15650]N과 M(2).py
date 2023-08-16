# https://www.acmicpc.net/problem/15650
# 백준-15650-N과 M(2)

import sys, itertools

input = sys.stdin.readline

n, m = map(int, input().split())

for p in itertools.combinations(range(1, n+1), m):
    print(' '.join(map(str, p)))