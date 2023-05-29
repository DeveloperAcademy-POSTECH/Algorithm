mushroom = []
for i in range(10):
    point = int(input())
    mushroom.append(point)
cnt = 0
for i in range(10):
    cnt += mushroom[i]
    if cnt > 100:  # cnt와 cnt-mushroom[i] 중 100에 더 가까운 수
        if abs(cnt - 100) <= abs(cnt - mushroom[i] - 100):
            print(cnt)
        else:
            print(cnt - mushroom[i])
        break
    if i == 9:
        print(cnt)
