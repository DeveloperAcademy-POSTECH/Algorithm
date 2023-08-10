T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 부분합
As = [0]
for i in range(n):
    As.append(As[i] + A[i])

Bs = [0]
for i in range(m):
    Bs.append(Bs[i] + B[i])

# Prefix Sum
PA = {}
PB = {}

for i in range(n+1):
    for j in range(i):
        k = As[i] - As[j]
        if PA.get(k, -1) == -1:
            PA[k] = 1
        else:
            PA[k] += 1

for i in range(m+1):
    for j in range(i):
        k = Bs[i] - Bs[j]
        if PB.get(k, -1) == -1:
            PB[k] = 1
        else:
            PB[k] += 1

result = 0
# find by all dictionary keys
for i in PA:
    n = T - i
    if PB.get(n, -1) != -1:
        result += PA[i]*PB[n]

print(result)