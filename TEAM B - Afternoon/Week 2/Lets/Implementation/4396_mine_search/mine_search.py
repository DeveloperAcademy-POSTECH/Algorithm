# n x n 격자, m 개의 지뢰
# 지뢰가 있는 지점을 건드리면 플레이어가 짐
# 한칸 주위 8칸의 지뢰가 몇개 있는지 알려줌
# . 은 지뢰없는 , * 는 지뢰, 이미 열린칸은 x
# 일부가 플레이된 게임의 정보를 읽어 해당하는 격자를 출력

# 처음 n 개의 줄은 플레이어가 누르지 않은 지뢰가 있는 맵
# 그 다음 n 개는 플레이어가 누른 지점
# 각 칸 주위에 지뢰가 몇개인지를 세서 채우자

# n 은 10보다 작거나 같음 -> 최대 100칸짜리 matrix
# -> 그냥 n^2 으로 다 돌아도 1초안에 충분할듯

# 아니 지뢰를 밟았어도 이미 열린 칸에 대해서는 지뢰가 몇 개 주변에 있는지도 표시해줘야한다네
import sys
sys.stdin = open("4396_mine_search/mine_search.txt", "r")

n = int(sys.stdin.readline())

# 1. 지뢰의 위치를 저장한 지도
mine_map = []
for _ in range(n):
    mine_map.append(list(sys.stdin.readline().rstrip()))

# 2. 사용자가 클릭한부분을 선택한 지도
user_map = []
for _ in range(n):
    user_map.append(list(sys.stdin.readline().rstrip()))



# 3. 주위 8칸 탐색을 위한 세팅
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 4. 각 user_map 을 돌면서 누른 지점이라면, 주위 8칸을 탐색
answer_matrix = []
flag = False # 지뢰를 터트린지 아닌지를 판단하는 flag

for i in range(0,len(user_map)):
    new_row = []
    for j in range(0,len(user_map[i])):
        if user_map[i][j] == "x": # 유저가 누른 지점이라면 주변탐색
            if mine_map[i][j] == "*":
                flag = True

            mine_cnt = 0
            for k in range(8): # 주위 8칸 중 한곳의 좌표
                ni = i + dr[k]
                nj = j + dc[k]

                if not((0<=ni<n) and (0<=nj<n)): # 만약 해당 좌표가 mine_map 을 넘어서면
                    continue

                if mine_map[ni][nj] == "*": # 해당 지점이 지뢰라면
                    mine_cnt += 1
            new_row.append(str(mine_cnt))
        else:
            new_row.append(".")
    answer_matrix.append(new_row)


if flag:
    for i in range(len(mine_map)):
        for j in range(len(mine_map[i])):
            if mine_map[i][j] == "*":
                answer_matrix[i][j] = "*"

for row in answer_matrix:
    print("".join(row))
    