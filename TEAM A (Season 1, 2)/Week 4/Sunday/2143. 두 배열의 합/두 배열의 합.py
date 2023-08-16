
t = int(input())
n = int(input())
nlist = list(map(int,input().split()))
m = int(input())
mlist = list(map(int,input().split()))

ndict  = {}
mdict = {}
answer = 0
for i in range(n):
    for j in range(i+1, n+1):
        tmp = sum(nlist[i:j])
        if tmp in ndict:
            ndict[tmp] += 1
        else:
            ndict[tmp] = 1

for i in range(m):
    for j in range(i+1, m +1):
        tmp = sum(mlist[i:j])
        if tmp in mdict:
            mdict[tmp] += 1
        else:
            mdict[tmp] = 1
for nkey in ndict.keys():
    if t-nkey in mdict.keys():
        answer += ndict[nkey] * mdict[t-nkey]
print(answer)
