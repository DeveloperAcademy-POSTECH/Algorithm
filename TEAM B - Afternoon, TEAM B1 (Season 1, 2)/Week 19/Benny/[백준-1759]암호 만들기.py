# https://www.acmicpc.net/problem/1759

import itertools

L, C = map(int, input().split())
alpha = input().split()
vowels = [a for a in alpha if a in ['a', 'e', 'i', 'o', 'u']] # 전체 모음이 아닌 입력 알파벳 중 모음만
consonants = [a for a in alpha if a not in vowels] # 마찬가지로 입력 알파벳 중 자음만(모음이 아닌 것)

possibles = []
for i in range(1, L - 1): # 1 ~ L-2 개의 모음에 대해서
    for t1 in itertools.combinations(vowels, i): # 전체 모음들 중 i개의 조합
        for t2 in itertools.combinations(consonants, L - i): # 전체 자음들 중 L-i개의 조합
            possibles.append(sorted(t1+t2)) # 모음셋, 자음셋 순서로 더해지므로 sorting해준 후 append
               
possibles = sorted(map(''.join, possibles)) # 알파벳 순이 아니라 모음 순서대로 들어가 있으므로 한번 더 sorting
for p in possibles:
    print(p)