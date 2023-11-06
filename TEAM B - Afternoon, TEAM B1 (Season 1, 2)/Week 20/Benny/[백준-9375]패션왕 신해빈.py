# https://www.acmicpc.net/problem/9375

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        item, item_type = input().split()
        if item_type in clothes.keys():
            clothes[item_type] += 1
        else:
            clothes[item_type] = 1
            
    count = 1
    for item_type in clothes.keys():
        count *= clothes[item_type] + 1
    
    print(count - 1)