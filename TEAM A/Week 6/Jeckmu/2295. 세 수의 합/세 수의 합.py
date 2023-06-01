N = int(input())

# 오름차순 정렬된 dictionary
s = []
for _ in range(N):
    s.append(int(input()))

s = {i: 1 for i in sorted(s)}

u = s.keys()

sum_xy = dict()
for x in u:
    for y in u:
        sum_xy[x+y] = 1

result = []
for z in u:
    for k in u:
        if sum_xy.get(k-z, -1) == 1:
            result.append(k)

print(max(result))