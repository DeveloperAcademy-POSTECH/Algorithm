# 백준. 2798. 블랙잭.
# 풀이1
n, m = map(int, input().split())
cards = list(set(map(int, input().split())))

max_sum = 0

for i in range(len(cards) - 2):
    for j in range(i+1, len(cards) - 1):
        for k in range(j+1, len(cards)):
            if cards[i] + cards[j] + cards[k] <= m:
                max_sum = max(max_sum, cards[i] + cards[j] + cards[k])
            
print(max_sum)

# 풀이 2
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
    