N = int(input())

fav = dict()
for _ in range(N**2):
    a = list(map(int, input().split()))
    fav[a[0]] = a[1:]

seat = [[0]*N for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def selectSeat(student):
    # 1번 조건은 우선도에 1 추가, 2번 조건은 우선도에 0.1 추가
    priority = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                # 범위를 벗어나지 않았는지
                if 0 <= nr < N and 0 <= nc < N:
                    # 좋아하는 학생이 있는 칸일 시 우선도 +10
                    if seat[nr][nc] in fav[student]:
                        priority[r][c] += 10
                    # 빈 칸일 시 우선도 +1
                    if seat[nr][nc] == 0:
                        priority[r][c] += 1

    # 우선도가 가장 높은 seat의 row, col을 return. 이미 우선도가 높은 좌석에 학생이 앉아 있다면 pass.
    # 우선도가 같은 것이 나왔다면, topList에 저장.
    # 이후 topList를 row, col 오름차순 정렬 후 첫 번째 것을 return.
    nowP = -100
    topList = []
    for r in range(N):
        for c in range(N):
            if priority[r][c] > nowP and seat[r][c] == 0:
                nowP = priority[r][c]
                topList = [(r, c)]
            elif priority[r][c] > nowP and seat[r][c] == 0:
                topList.append((r, c))

    topList = list(sorted(topList, key=lambda x: (x[0], x[1]), reverse=True))
    return topList[0]


# 학생들 앉히기
for student in fav.keys():
    i, j = selectSeat(student)
    seat[i][j] = student


def calculateSatisfaction(r, c):
    favStuCnt = 0
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        # 범위를 벗어나지 않았는지
        if 0 <= nr < N and 0 <= nc < N:
            # 좋아하는 학생이 있는 칸일 때 count++
            if seat[nr][nc] in fav[seat[r][c]]:
                favStuCnt += 1

    if favStuCnt == 0:
        return 0
    else:
        return 10**(favStuCnt-1)


satisfactionResult = 0
for i in range(N):
    for j in range(N):
        satisfactionResult += calculateSatisfaction(i, j)

print(satisfactionResult)