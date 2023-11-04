# https://www.acmicpc.net/problem/14890

import sys

input = sys.stdin.readline

n, l = map(int, input().split())

the_map = []
for _ in range(n):
    the_map.append(list(map(int, input().split())))

count = 2 * n
for row in range(n):
    lengths = [1]
    pre_h = the_map[row][0]
    for col in range(1, n):
        if pre_h == the_map[row][col]:
            lengths[-1] += 1
        elif abs(pre_h - the_map[row][col]) > 1:
            lengths.append(-100)
        else:
            if pre_h > the_map[row][col]:
                lengths.append(-l+1)
            else:
                lengths[-1] -= l
                lengths.append(1)
            pre_h = the_map[row][col]

    for length in lengths:
        if length < 0:
            count -= 1
            break
            
for col in range(n):
    lengths = [1]
    pre_h = the_map[0][col]
    for row in range(1, n):
        if pre_h == the_map[row][col]:
            lengths[-1] += 1
        elif abs(pre_h - the_map[row][col]) > 1:
            lengths.append(-100)
        else:
            if pre_h > the_map[row][col]:
                lengths.append(-l+1)
            else:
                lengths[-1] -= l
                lengths.append(1)
            pre_h = the_map[row][col]

    for length in lengths:
        if length < 0:
            count -= 1
            break
            
print(count)