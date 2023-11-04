# https://www.acmicpc.net/problem/12015

import sys

input = sys.stdin.readline

n = int(input())
seq = [0] + list(map(int, input().split()))
lis = [0, 1]
min_value = [0, seq[1]]

def binary_search():
    left, right = 0, len(min_value)-1
    while left <= right:
        mid = (left + right) // 2
        if min_value[mid] < seq[i]:
            left = mid + 1
        else:
            right = mid - 1
            
    return mid if min_value[mid] < seq[i] else mid-1

for i in range(2, n+1):
    lis.append(binary_search() + 1)
    if len(min_value) - 1 < lis[i]:
        min_value.append(seq[i])
    elif seq[i] < min_value[lis[i]]:
        min_value[lis[i]] = seq[i]
        
print(max(lis))

    
    
    
    