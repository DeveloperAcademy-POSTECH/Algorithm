from collections import deque
import sys

read = sys.stdin.readline


def find(x):
    if dock[x] == x:
        return x

    k = find(dock[x])
    dock[x] = k
    return k


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        dock[y] = x
    else:
        dock[x] = y


gate = int(read().strip("\n"))

air = deque([])
for _ in range(int(read().strip("\n"))):
    air.append(int(read().strip("\n")))

dock = {i: i for i in range(0, gate+1)}
docked = 0

for i in air:
    x = find(i)

    if x == 0:
        break
    union(x, x-1)
    docked += 1

print(docked)
