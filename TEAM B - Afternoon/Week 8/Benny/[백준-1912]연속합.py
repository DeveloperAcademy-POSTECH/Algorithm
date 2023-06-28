import sys

input = sys.stdin.readline

n = int(input())
integers = list(map(int, input().split()))

for i in range(1, len(integers)):
    integers[i] += max(0, integers[i-1])
    
print(max(integers))