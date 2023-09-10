#완전탐색_소수찾기
from itertools import permutations

def solution(numbers):
    nums = [int(i) for i in numbers]
    result = set()


    for length in range(1, len(nums) + 1):
        for combination in permutations(nums, length):
            tmpNum = int(''.join(map(str, combination)))
            if checkPrime(tmpNum):
                result.add(tmpNum)

    return len(result)

def checkPrime(N):
    if N <= 1:
        return False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True