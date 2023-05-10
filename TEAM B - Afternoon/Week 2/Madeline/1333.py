#1333

N, L, D = map(int, input().split())

# 총 플레이 시간
total = N * L + 5 * (N - 1)

play = [0] * total
for i in range(0, total, L + 5):
    for j in range(i, i + L):
        play[j] = 1
for i in range(0, total, D):
    if play[i] == 0:
        print(i)
        break
else:
    print(i + D)
# for문에도 else 가 있구나..!