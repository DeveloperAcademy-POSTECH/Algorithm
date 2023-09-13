# https://www.acmicpc.net/problem/2473
# 백준-2473-세 용액

import sys

input = sys.stdin.readline

n = int(input())
values = sorted(list(map(int, input().split())))

min_sum = abs(sum(values[:3]))
comb = [values[0], values[1], values[2]]

for i in range(len(values)-2):
    left = i+1
    right = len(values)-1
    while left < right:
        result = values[i] + values[left] + values[right]
        if abs(result) < min_sum:
            min_sum = abs(result)
            comb = [values[i], values[left], values[right]]

        if result < 0:
            left += 1

        elif result > 0:
            right -= 1

        else:
            comb = [values[i], values[left], values[right]]
            break
        
print(' '.join(map(str, comb)))
        
    
    