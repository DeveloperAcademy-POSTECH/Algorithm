# 백준-2467-용액
# https://www.acmicpc.net/problem/2467

import sys

input = sys.stdin.readline

def find(cur_idx):
    global values
    left = cur_idx + 1
    right = len(values) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid == 0:
            if abs(values[cur_idx] + values[mid]) < abs(values[cur_idx] + values[mid+1]):
                return abs(values[cur_idx] + values[mid]), values[cur_idx], values[mid] 
            else:
                return abs(values[cur_idx] + values[mid+1]), values[cur_idx], values[mid+1] 
        
        elif mid == len(values) - 1:
            return abs(values[cur_idx] + values[mid]), values[cur_idx], values[mid]
        
        if abs(values[cur_idx] + values[mid-1]) < abs(values[cur_idx] + values[mid]):
            right = mid - 1
            
        elif abs(values[cur_idx] + values[mid]) > abs(values[cur_idx] + values[mid+1]):
            left = mid + 1
            
        else:
            return abs(values[cur_idx] + values[mid]), values[cur_idx], values[mid]
    
    return abs(values[cur_idx] + values[mid]), values[cur_idx], values[mid]
            
        

n = int(input())
values = list(map(int, input().split()))

min_sum = abs(values[0] + values[1])
value_a, value_b = values[0], values[1]
for i in range(n-2):
    temp_min_sum, a, b = find(i)
    if temp_min_sum < min_sum:
        value_a, value_b = a, b
        min_sum = temp_min_sum
        
if abs(values[-2] + values[-1]) < min_sum:
    value_a, value_b = values[-2], values[-1]
        
print(value_a, value_b)