# 백준 1644번: 소수의 연속합

import sys
import math

input = sys.stdin.readline

# N <= 4 * 10^6
N = int(input())

if N == 1: # 예외 처리
    print(0)
    sys.exit(0)

arr = [True for _ in range(N + 1)]

for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i]:
        j = 2

        while i * j <= N:
            arr[i * j] = False
            j += 1

primes = [i for i in range(2, N + 1) if arr[i]]
# print(primes)

left, right = 0, 0
current_sum = primes[0]
answer = 0
len_primes = len(primes)

# print(len_primes)

while True:
    # print(primes[left : right + 1])

    if current_sum < N:
        if right < len_primes - 1:
            right += 1
            current_sum += primes[right]
        else: break
    else:
        if current_sum == N:
            answer += 1
        current_sum -= primes[left]
        left += 1

print(answer)
