from itertools import permutations
def solution(numbers):
    def isPrime(n: int):
        for i in range(2, n):
            if n%i == 0:
                return False
        return True

    num = set()

    for i in range(1, len(numbers)+1):
        num.update(set(map(int, map(''.join, permutations(numbers, i)))))

    answerSet = set()

    for n in num:
        if n == 1 or n == 0:
            continue
        if isPrime(n):
            answerSet.add(n)

    return len(answerSet)