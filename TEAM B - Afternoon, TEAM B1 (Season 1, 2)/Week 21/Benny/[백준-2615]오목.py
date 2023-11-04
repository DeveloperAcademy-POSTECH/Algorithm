# https://www.acmicpc.net/problem/2615

board = []
for _ in range(19):
    board.append(list(map(int, input().split())))
    
def check(row, col):
    black_counts = [0, 0, 0, 0]
    white_counts = [0, 0, 0, 0]
    
    # 가로로 5개
    for d in range(5):
        nr, nc = row, col+d
        if 0 <= nr < 19 and 0 <= nc < 19:
            if board[nr][nc] == 1:
                black_counts[0] += board[nr][nc]
            elif board[nr][nc] == 2:
                white_counts[0] += board[nr][nc] 
    
    if 0 <= row < 19 and 0 <= col-1 < 19 and board[row][col-1] == 1:
        black_counts[0] = 0
    if 0 <= row < 19 and 0 <= col+5 < 19 and board[row][col+5] == 1:
        black_counts[0] = 0
        
    if 0 <= row < 19 and 0 <= col-1 < 19 and board[row][col-1] == 2:
        white_counts[0] = 0
    if 0 <= row < 19 and 0 <= col+5 < 19 and board[row][col+5] == 2:
        white_counts[0] = 0
        
    # 세로로 5개
    for d in range(5):
        nr, nc = row+d, col
        if 0 <= nr < 19 and 0 <= nc < 19:
            if board[nr][nc] == 1:
                black_counts[1] += board[nr][nc]
            elif board[nr][nc] == 2:
                white_counts[1] += board[nr][nc] 
    
    if 0 <= row-1 < 19 and 0 <= col < 19 and board[row-1][col] == 1:
        black_counts[1] = 0
    if 0 <= row+5 < 19 and 0 <= col < 19 and board[row+5][col] == 1:
        black_counts[1] = 0
        
    if 0 <= row-1 < 19 and 0 <= col < 19 and board[row-1][col] == 2:
        white_counts[1] = 0
    if 0 <= row+5 < 19 and 0 <= col < 19 and board[row+5][col] == 2:
        white_counts[1] = 0
        
    # 우하향 대각선으로 5개
    for d in range(5):
        nr, nc = row+d, col+d
        if 0 <= nr < 19 and 0 <= nc < 19:
            if board[nr][nc] == 1:
                black_counts[2] += board[nr][nc]
            elif board[nr][nc] == 2:
                white_counts[2] += board[nr][nc] 
                
    if 0 <= row-1 < 19 and 0 <= col-1 < 19 and board[row-1][col-1] == 1:
        black_counts[2] = 0
    if 0 <= row+5 < 19 and 0 <= col+5 < 19 and board[row+5][col+5] == 1:
        black_counts[2] = 0
        
    if 0 <= row-1 < 19 and 0 <= col-1 < 19 and board[row-1][col-1] == 2:
        white_counts[2] = 0
    if 0 <= row+5 < 19 and 0 <= col+5 < 19 and board[row+5][col+5] == 2:
        white_counts[2] = 0
        
    # 우상향 대각선으로 5개
    for d in range(5):
        nr, nc = row-d, col+d
        if 0 <= nr < 19 and 0 <= nc < 19:
            if board[nr][nc] == 1:
                black_counts[3] += board[nr][nc]
            elif board[nr][nc] == 2:
                white_counts[3] += board[nr][nc] 
    
    if 0 <= row+1 < 19 and 0 <= col-1 < 19 and board[row+1][col-1] == 1:
        black_counts[3] = 0
    if 0 <= row-5 < 19 and 0 <= col+5 < 19 and board[row-5][col+5] == 1:
        black_counts[3] = 0
        
    if 0 <= row+1 < 19 and 0 <= col-1 < 19 and board[row+1][col-1] == 2:
        white_counts[3] = 0
    if 0 <= row-5 < 19 and 0 <= col+5 < 19 and board[row-5][col+5] == 2:
        white_counts[3] = 0
        
    return black_counts, white_counts
            
blacks = []
whites = []
for i in range(19*19):
    r, c = i // 19, i % 19
    black_counts, white_counts = check(r, c)
    
    if 5 in black_counts:
        blacks.append((r, c))
    if 10 in white_counts:
        whites.append((r, c))
        
blacks = sorted(blacks, key=lambda x: (x[1], x[0]))
whites = sorted(whites, key=lambda x: (x[1], x[0]))

if blacks and whites:
    print(0)
elif blacks and whites == []:
    print(1)
    print(blacks[0][0]+1, blacks[0][1]+1)
elif whites and blacks == []:
    print(2)
    print(whites[0][0]+1, whites[0][1]+1)
else:
    print(0)

        
    