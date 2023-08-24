from itertools import permutations
import math

def primeNumber(number):
    for i in range (2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True 

def solution(numbers):
    answer = 0
    result = []
    array = list(numbers)
    for i in range(len(numbers)):
        cases = list(permutations(array, i + 1))
        for case in cases:
            case = ''.join(case)
            if int(case) > 1 and primeNumber(int(case)):
                result.append(int(case))
    print(result, set(result))
    answer = len(set(result))
    return answer