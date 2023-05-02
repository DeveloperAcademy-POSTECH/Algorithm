
dwarfList = [int(input()) for _ in range(9)]

dwarfList.sort()
dwarfSum = sum(dwarfList)

# 7명의 합이 100이 되는 것이 아닌 2명을 제외한 값이 100이 되는 경우를 찾기
for i in range(len(dwarfList)):
    for j in range(i + 1, len(dwarfList)):
        if dwarfSum - (dwarfList[i] + dwarfList[j]) == 100:
            for index in range(len(dwarfList)):
                if index == i or index == j:
                    pass
                else:
                    print(dwarfList[index])
            exit()