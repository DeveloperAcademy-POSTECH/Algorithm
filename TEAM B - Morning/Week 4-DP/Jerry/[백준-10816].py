n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

cnt = {}
for i in a:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in b:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')