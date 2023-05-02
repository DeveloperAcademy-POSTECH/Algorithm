# 백준. 2798. 블랙잭.
from itertools import combinations

n, m = map(int, input().split())
cards = set(map(int, input().split()))

combis = list(combinations(cards, 3))
max_sum = 0

for combi in combis:
    temp_sum = sum(combi)
    if temp_sum <= m:
        max_sum = max(max_sum, temp_sum)
        
print(max_sum)
    