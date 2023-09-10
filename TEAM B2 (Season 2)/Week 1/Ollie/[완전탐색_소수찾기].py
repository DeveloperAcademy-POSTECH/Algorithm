# https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    len_num = len(numbers)
    max_num = int(max(list(numbers)) * len_num)
    is_prime = [False, False, True] + [True] * (max_num-2)
    for i in range(2, int(max_num**.5)+1):
        if is_prime[i]:
            for j in range(i*2, max_num+1, i):
                is_prime[j] = False
    
    new_nums = set()
    for i in range(1, len_num+1):
        for p in permutations(range(len_num), i):
            new_num = ''
            for idx in p:
                new_num += numbers[idx]
            new_nums.add(int(new_num))

    return [is_prime[i] for i in new_nums].count(True)