table = [["EMPTY"]*51 for _ in range(51)]
ufTable = [[(r, c) for c in range(51)] for r in range(51)]
answer = []


def update(r, c, value):
    # 연결된 제일 상위 root 셀에 value 삽입.
    nr, nc = find(r, c)
    table[nr][nc] = value


def updateValue(v1, v2):
    # 모든 셀의 값을 검색하며 update.
    for i in range(51):
        for j in range(51):
            if table[i][j] == v1:
                table[i][j] = v2


def merge(r1, c1, r2, c2):
    nr1, nc1 = find(r1, c1)
    nr2, nc2 = find(r2, c2)

    if table[nr1][nc1] != "EMPTY":
        union(nr1, nc1, nr2, nc2)
    else:
        # 항상 (r1,c1)쪽으로 연결함과 동시에, (r2,c2)에만 값이 있다면 그 값을 (r1,c1)으로 옮겨오며 연결.
        if table[nr2][nc2] != "EMPTY":
            table[nr1][nc1] = table[nr2][nc2]

        union(nr1, nc1, nr2, nc2)


def unMerge(r, c):
    nr, nc = find(r, c)
    # 우선 param으로 받은 (r, c)셀에 연결된 root 셀에 값이 있다면, 저장해둠
    temp = table[nr][nc]

    tempList = []
    # 그 후, 연결된 셀들의 병합을 모두 해제 -> 모든 셀들의 root셀을 find하며, root셀이 같다면 연결 해제 후, 해제한 셀 값들은 초기화
    # 찾을 때마다 병합 해제를 하면, 연결된 모든 셀을 찾을 수 없으므로, 저장해뒀다가 한번에 해제
    for i in range(51):
        for j in range(51):
            if find(i, j) == (nr, nc):
                tempList.append((i, j))

    for t in tempList:
        i, j = t
        table[i][j] = "EMPTY"
        ufTable[i][j] = (i, j)

    # 아까 저장한 그 값을 (r, c)로 옮겨옴
    table[r][c] = temp


def print_(r, c):
    nr, nc = find(r, c)
    answer.append(table[nr][nc])


# Union-Find
def find(r, c):
    if (r, c) == ufTable[r][c]:
        return ufTable[r][c]

    nr, nc = ufTable[r][c]
    ufTable[r][c] = find(nr, nc)
    return ufTable[r][c]


def union(r1, c1, r2, c2):
    ufTable[r2][c2] = ufTable[r1][c1]


def solution(commands):
    for command in commands:
        c = list(command.split())

        if c[0] == "UPDATE":
            if len(c) == 4:
                # update r c value
                update(int(c[1]), int(c[2]), c[3])
            else:
                # update value1 value2
                updateValue(c[1], c[2])

        elif c[0] == "MERGE":
            merge(int(c[1]), int(c[2]), int(c[3]), int(c[4]))

        elif c[0] == "UNMERGE":
            unMerge(int(c[1]), int(c[2]))

        elif c[0] == "PRINT":
            print_(int(c[1]), int(c[2]))
    return answer