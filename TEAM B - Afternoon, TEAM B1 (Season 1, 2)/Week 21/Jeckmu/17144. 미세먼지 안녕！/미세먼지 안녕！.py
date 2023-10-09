import copy
R, C, T = map(int, input().split())

g = []
for _ in range(R):
    g.append(list(map(int, input().split())))
    
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

newG = [[0]*C for _ in range(R)]
            
# 확산
def diffusion(r, c):
    if g[r][c] == -1:
        newG[r][c] = -1
        return

    diffusionCnt = 0
    diffusionAmount = int(g[r][c]/5)
    for i in range(4):
        lr = r+dr[i]
        lc = c+dc[i]
        
        # 칸이 없거나, 공기청정기가 존재한다면
        if lr < 0 or lr >= R or lc < 0 or lc >= C or g[lr][lc] == -1:
            continue
        
        newG[lr][lc] += diffusionAmount
        diffusionCnt += 1
        
    newG[r][c] += g[r][c] - (diffusionAmount * diffusionCnt)

# 공기청정기는 항상 1열이므로, 몇 행인지만 저장.
purifier = []
for i in range(R):
    if g[i][0] == -1:
        purifier.append(i)

# 공기청정기 바람        
def wind():
    # ----- 위쪽 공기청정기의 바람은 반시계방향으로 순환 -----
    
    # 위쪽 공기청정기 바로 위부터 (0, 0)까지 한 칸씩 아래로 당기기
    for i in range(purifier[0]-1, 0, -1):
        g[i][0] = g[i-1][0]
    
    # 1행 (r == 0) 왼쪽으로 당기기
    for i in range(C-1):
        g[0][i] = g[0][i+1]
        
    # C열 위로 당기기
    for i in range(purifier[0]):
        g[i][C-1] = g[i+1][C-1]
        
    # 위쪽 공기청정기가 있는 행, 오른쪽으로 밀기
    for i in range(C-1, 1, -1):
        g[purifier[0]][i] = g[purifier[0]][i-1]
    g[purifier[0]][1] = 0
    
    # ----- 아래쪽 공기청정기의 바람은 시계방향으로 순환 -----
    
    # 아래쪽 공기청정기 바로 아래부터 (R-1, 0)까지 한 칸씩 위로 당기기
    for i in range(purifier[1]+1, R-1, 1):
        g[i][0] = g[i+1][0]
    
    # R행 왼쪽으로 당기기
    for i in range(C-1):
        g[R-1][i] = g[R-1][i+1]
        
    # C열 아래로 당기기
    for i in range(R-1, purifier[1], -1):
        g[i][C-1] = g[i-1][C-1]
        
    # 아래쪽 공기청정기가 있는 행, 오른쪽으로 밀기
    for i in range(C-1, 1, -1):
        g[purifier[1]][i] = g[purifier[1]][i-1]
    g[purifier[1]][1] = 0


for _ in range(T):
    for r in range(R):
        for c in range(C):
            diffusion(r, c)

    g = copy.deepcopy(newG)
    newG = [[0]*C for _ in range(R)]

    wind()

print(sum(map(sum, g)) + 2)