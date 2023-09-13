# 백준-15663-N과 M(9)
# https://www.acmicpc.net/problem/15663

import sys, itertools

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

if m == 1:
    seqs = sorted(set(nums))
    for seq in seqs:
        print(seq)
else:
    seqs = sorted(set(itertools.permutations(nums, m)))
    for seq in seqs:
        print(' '.join(map(str, seq)))
