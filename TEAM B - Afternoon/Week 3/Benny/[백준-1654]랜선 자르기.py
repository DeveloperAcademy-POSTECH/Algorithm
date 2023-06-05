# https://www.acmicpc.net/problem/1654
# 백준 - 1654 - 랜선 자르기

import sys

def get_number_of_wires(wires, length):
    count = 0
    for wire in wires:
        print(f"{wire} // {length} = {wire // length}")
        count += wire // length

    print(f"count: {count}")
    print()
    return count

k, n = map(int, sys.stdin.readline().split())
wires = []
for _ in range(k):
    wires.append(int(sys.stdin.readline().rstrip()))
    
left, right = 1, min(wires)
max_length = 0
while left <= right:
    mid = (left + right) // 2
    print(f"left: {left}, right: {right}, mid: {mid}")
    if get_number_of_wires(wires, mid) >= n:
        max_length = max(max_length, mid)
        left = mid + 1
    else:
        right = mid - 1
        
print(max_length)
        

