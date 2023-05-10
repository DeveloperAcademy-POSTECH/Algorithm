import sys
sys.stdin = open("11651_sorting_coordinates2/sorting_coordinates2.txt", "r")

N = int(sys.stdin.readline())


# dictionary 에 key: x - value: [y] 로 넣기
coordinates = {}

for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    if coordinates.get(y) == None:
        coordinates[y] = [x]
    else:
        coordinates[y].append(x)

# key 인 x 를 ascending 으로 sorting
keys = list(coordinates.keys())
keys.sort()

# 각각의 y 를 ascending 으로 sorting
for key in keys:
    coordinates[key].sort()
    for value in coordinates[key]:
        print(value, key)


