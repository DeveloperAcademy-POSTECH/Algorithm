#https://www.acmicpc.net/problem/1717
#백준-1717-집합의 표현

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parents(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
        
n, m = map(int, input().split())
parents = [i for i in range(n+1)]
for _ in range(m):
    calc, a, b = map(int, input().split())
    if calc == 0:
        union_parents(parents, a, b)
    else:
        print("YES" if find_parent(parents, parents[a])==find_parent(parents, parents[b]) else "NO")