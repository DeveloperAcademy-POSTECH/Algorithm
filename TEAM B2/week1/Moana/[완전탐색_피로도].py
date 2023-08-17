#완전탐색_피로도

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    size = len(dungeons)
    
    for permute in permutations(dungeons, size):
        minLife = k
        count = 0 
        for per in permute:
            if minLife >= per[0]:
                minLife -= per[1]
                count += 1
            if count > answer:
                answer = count
    
    return answer