import bisect
N = int(input())

lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))

lines = sorted(lines, key=lambda x:x[0])

end = []
for s, e in lines:
    end.append(e)

res = []
for e in end:
    a = bisect.bisect_left(res, e)
    if a == len(res):
        res.append(e)
    else:
        res[a] = e
        
print(len(end)-len(res))