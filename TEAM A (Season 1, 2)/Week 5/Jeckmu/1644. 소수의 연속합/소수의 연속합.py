N = int(input())

nums = [True] * (N+1)
nums[0] = False
nums[1] = False

# 에라토스테네스의 체
for i in range(2, N+1):
    if not nums[i]:
        continue
    elif i > N:
        break

    k = 1
    while True:
        k += 1
        j = i*k
        if j > N:
            break
        nums[j] = False

primes = []
for i, flag in enumerate(nums):
    if flag:
        primes.append(i)

# two pointer of index
p1 = 0
p2 = 0
result = 0
while True:
    S = sum(primes[p1:p2])

    if S == N:
        p2 += 1
        result += 1
    elif S < N:
        p2 += 1
    elif S > N:
        p1 += 1

    if p1 > len(primes) or p2 > len(primes):
        break

print(result)