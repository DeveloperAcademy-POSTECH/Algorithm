N = int(input())

H = dict()

for _ in range(N):
    command, c, sec = input().split()
    sec = int(sec)
    H[sec] = (command, c, sec, True)

res = ""

for key in sorted(H.keys(), key=lambda x: -x):
    command, c, sec, flag = H[key]
    # if flag == False -> pass
    if not flag:
        continue

    if command == "type":
        res = c + res
    else:   # if command == "undo"
        sec, c = map(int, (sec, c))
        for k in H.keys():
            # 범위 안에 포함되지 않으면 pass
            if not (sec - c) <= k <= sec:
                continue

            if flag:
                H[k] = (command, c, sec, False)
            else:
                H[k] = (command, c, sec, True)

if res != "":
    print(res)