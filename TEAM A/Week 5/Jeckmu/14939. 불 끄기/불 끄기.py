import copy
from itertools import product
bulb = [list(input()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if bulb[i][j] == "#":
            bulb[i][j] = 0
        else:
            bulb[i][j] = 1


def toggle(B, i, j):
    B[i][j] = (B[i][j] + 1) % 2
    if i+1 < 10:
        B[i+1][j] = (B[i+1][j] + 1) % 2
    if i-1 >= 0:
        B[i-1][j] = (B[i-1][j] + 1) % 2
    if j+1 < 10:
        B[i][j+1] = (B[i][j+1] + 1) % 2
    if j-1 >= 0:
        B[i][j-1] = (B[i][j-1] + 1) % 2


results = []

# 첫 줄의 경우의 수 2^10 가지
isToggles = list(product([0, 1], repeat=10))

for isToggle in isToggles:
    result = 0
    b = copy.deepcopy(bulb)

    # 첫 줄 세팅
    for i, k in enumerate(isToggle):
        if k == 1:
            toggle(b, 0, i)
            result += 1

    # 2~10째줄
    for i in range(1, 10):
        for j in range(0, 10):
            # 바로 위 전구가 켜져 있다면 toggle.
            if b[i-1][j] == 1:
                toggle(b, i, j)
                result += 1

    # 모든 전구가 꺼져 있다면 성공.
    if max(map(max, b)) == 0:
        results.append(result)

if len(results) == 0:
    print(-1)
else:
    print(min(results))