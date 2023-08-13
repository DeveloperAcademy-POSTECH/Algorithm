dwarf = []
for i in range(9):
    height = int(input())
    dwarf.append(height)

# 9명 중에 2명 골라서 빼고 나머지 합이 100인 경우를 찾으면 되겠다.
total = sum(dwarf)
fake1 = 0
fake2 = 0

for i in range(9):#0~8
    for j in range(i+1, 9):#~8
        if total == 100 + dwarf[i] + dwarf[j]:
            # dwarf.remove(dwarf[i])
            # dwarf.remove(dwarf[j])
            fake1 = dwarf[i]
            fake2 = dwarf[j]
            break
dwarf.remove(fake1)
dwarf.remove(fake2)
dwarf.sort()
for i in range(7):
    print(dwarf[i])