a = int(input())
num = 2
def prime_list(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    return [i for i in range(2,n+1 ) if sieve[i] == True]
primelist = prime_list(a)
low, high, cnt = 0,0,0
while True:
    if(sum(primelist[low:high])) >a:
        low+=1
    elif(sum(primelist[low:high])) == a:
        cnt += 1
        low += 1
    elif high == len(primelist):
        break
    else:
        high +=1
print(cnt)