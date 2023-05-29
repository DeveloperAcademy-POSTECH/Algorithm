import math

N, M, K = map(int, input().split())


def combination(a, b):
    if a < b:
        return 0
    else:
        return math.factorial(a) / math.factorial(a - b) * math.factorial(b)

answer = 0
for k in range(K, N):
    answer += (combination(N-M, M-k) * combination(M,k)) / combination(N,M)
print(answer)