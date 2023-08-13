n, k = map(int, input().split())
count = 0

# 가능한 나눗셈을 하는 횟수를 많이 늘려야, count의 수를 최소화 가능하다.

while True :
    if n % k == 0 : 
        n = n//k
    else :
        n = n-1
    count += 1
    if n == 1 :
        break

print(count)
