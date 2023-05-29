# 좌표 x, y 가 주어짐
# 우선 x 가 즈으가하는 순으로, x 가 같으면 y 가 증가하는 순으로 정렬
# 좌표의 갯수 N 은 100,000 -> nLog(n) 정도면 괜찮을듯?

# key 를 이용해서 두개를 정렬시키고 싶은데 되려나?
# 찾아보니 python 의 sort 는 stable 이구만
# stable? -> 정렬을 할때 같은 기준의 두개의 객체는 정렬이 끝나도 순서 유지
# e.g) 스페이드 5 와 다이아 5 카드가 붙어있고 카드의 숫자순으로 정렬하면
# stable 정렬이면 정렬이 끝나도 스페이드 5 와 다이아 5 의 순서는 같음

# 그렇다면 우선 하나의 key 로 정렬하고, 그 다음 다른 기준으로 정렬시키면 순서는 유지되면서 해당 key 에 대해서만 되는건가?
# 아예 처음에 dictionary 로 만들어서 다 넣고, 해당 dict 안에서 정렬하는게 낫지 않을까?
# -> 둘 다 해봤는데 방법 1은 332ms, 방법 2는 372ms. 어디서 차이가 나는걸까?

import sys
sys.stdin = open("11650_sorting_coordinates/sorting_coordinates.txt", "r")

N = int(sys.stdin.readline())


# # 방법 1: stable sort 를 다룰 줄 몰라서 dict 에 넣고 넣은것을 sort 함
# # dictionary 에 key: x - value: [y] 로 넣기
# coordinates = {}

# for _ in range(N):
#     x, y = list(map(int, sys.stdin.readline().split()))
#     if coordinates.get(x) == None:
#         coordinates[x] = [y]
#     else:
#         coordinates[x].append(y)

# # key 인 x 를 ascending 으로 sorting
# keys = list(coordinates.keys())
# keys.sort()

# # 각각의 y 를 ascending 으로 sorting
# for key in keys:
#     coordinates[key].sort()
#     for value in coordinates[key]:
#         print(key, value)



# 방법 2: stable sort 라는 사실을 이용한 두번 sort
coordinates = []
for _ in range(N):
    coordinates.append(list(map(int, sys.stdin.readline().split())))

coordinates.sort(key = lambda x : x[1])
coordinates.sort(key = lambda x : x[0])

for coordinate in coordinates:
    print(f"{coordinate[0]} {coordinate[1]}")
