past = input()
k = int(input())

front = past[:k]
back = past[-k:]

res = 0

if len(past)/2 >= k:
    for i in range(k):
        if front[i] != back[i]:
            res += 1
else:
    # 간격 n
    n = len(past)-k

    for i in range(n):
        p = i
        cnt = dict()
        while p < len(past):
            if cnt.get(past[p]):
                cnt[past[p]] += 1
            else:
                cnt[past[p]] = 1

            p += n

        # 최대인 key값
        m = max(cnt, key=cnt.get)
        for key in cnt.keys():
            if key == m:
                continue
            res += cnt[key]

print(res)
