# https://www.acmicpc.net/submit/1806/66829841

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
seq = list(map(int, input().split()))

left, right = 0, 0
sub_sum = seq[0]
min_len = len(seq) + 1

while left <= right:
    if sub_sum >= s:
        min_len = min(min_len, right - left + 1)
        sub_sum -= seq[left]
        left += 1
    else:
        if right == len(seq) - 1:
            break
        right += 1
        sub_sum += seq[right]
        
print(0 if min_len == len(seq) + 1 else min_len)