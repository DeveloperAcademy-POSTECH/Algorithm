b = []

for _ in range(19):
    b.append(list(map(int, input().split())))
  
# 아래로 5개, 우하향 대각선 5개, 오른쪽으로 5개, 우상향 대각선 5개 (그러나, 6목 방지를 위해 시작에서 한칸 전부터, 5목이 되기 한칸 뒤까지 포함)
dr = [[-1, 1, 2, 3, 4, 5], [-1, 1, 2, 3, 4, 5], [0, 0, 0, 0, 0, 0], [1, -1, -2, -3, -4, -5]]
dc = [[0, 0, 0, 0, 0, 0], [-1, 1, 2, 3, 4, 5], [-1, 1, 2, 3, 4, 5], [-1, 1, 2, 3, 4, 5]]

# 체크
for r in range(19):
    for c in range(19):
        if b[r][c] == 0:
            continue

        for j in range(4):
            cnt = 0
            for i in range(6):
                lr = r + dr[j][i]
                lc = c + dc[j][i]
                
                # 6목 이상 제외
                if i == 0 or i == 5:
                    if lr < 0 or lr >= 19 or lc < 0 or lc >= 19 or b[lr][lc] != b[r][c]:
                        cnt += 1
                else:
                    if lr < 0 or lr >= 19 or lc < 0 or lc >= 19:
                        continue
                    if b[lr][lc] == b[r][c]:
                        cnt += 1
            
            if cnt == 6:
                print(b[r][c])
                print(r+1, c+1)
                exit()

# 승부 결정 x
print(0)