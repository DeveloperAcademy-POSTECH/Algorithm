#백준. 1018. 체스판 다시 칠하기
def get_paint_count(start_row_idx, start_col_idx):
    count1 = 0
    count2 = 0
    for i in range(start_row_idx, start_row_idx + 8):
        for j in range(start_col_idx, start_col_idx + 8):
            if input_board[i][j] != sample_board1[i][j]:
                count1 += 1
            if input_board[i][j] != sample_board2[i][j]:
                count2 += 1
                
    return min(count1, count2)
    
n, m = map(int, input().split())
input_board = []
for _ in range(n):
    input_board.append(list(input()))

sample_board1 = [['B' if (i+j)%2 == 0 else 'W' for j in range(m)] for i in range(n)]
sample_board2 = [['W' if (i+j)%2 == 0 else 'B' for j in range(m)] for i in range(n)]

min_count = 64

for i in range(n-7):
    for j in range(m-7):
        min_count = min(min_count, get_paint_count(i, j))
        
print(min_count)