- 2003, 수들의 합2
```py
# 시간초과
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# cnt = 0

# # 첫 포인터
# for i in range(0, len(arr)):
#     # i부터 끝까지를 반복한다.
#     for j in range(i, len(arr)):
#         # 만약 i부터 j까지의 배열 합이 m 이라면
#         if sum(arr[i:j+1]) == m:
#             # 카운트를 1 늘리고 j 반복을 끝낸다.
#             cnt += 1
#             break

# print(cnt)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 1
cnt = 0

while True:
    if right > n or left > right:
        break

    tol = sum(arr[left: right])
    if tol == m:
        cnt += 1
        right += 1

    elif tol < m:
        right += 1

    else:
        left += 1

print(cnt)
```
---

- 1476, 날짜 계산
```py
# e <= 15
# s <= 28
# m <= 19

e, s, m = 1, 1, 1
targetE, targetS, targetM = map(int, input().split())
current = 1

while True:
    if targetS == s and targetE == e and targetM == m:
        break

    current += 1
    e += 1
    s += 1
    m += 1

    if e > 15:
        e = 1
        
    if s > 28:
        s = 1

    if m > 19:
        m = 1

print(current)
```

- 4673, 셀프 넘버
```py
arr = [i for i in range(0,10001)]
tmp = []

for i in arr:
    # 생성자 확인하기
    selfNum = i + sum(map(int, str(i)))
    # 생성자가 없으면 나중에 지우기
    if selfNum <= 10000:
        tmp.append(selfNum)

answer = set(arr) - set(tmp)
for num in sorted(list(answer)):
    print(num)
```

- 2309, 일곱 난쟁이
```py
arr = [int(input()) for _ in range(9)]

for i in arr:
    for j in arr:
        if sum(arr) - i - j == 100 and i != j:
            arr.remove(i)
            arr.remove(j)

arr.sort()            
for i in arr:
    print(i)
```
