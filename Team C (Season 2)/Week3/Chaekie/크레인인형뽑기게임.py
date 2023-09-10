# 3중 for문
def solution1(board, moves):    
    answer = 0
    stack = []
    
    for move in moves:
        for j in range(len(board[0])):
            for i in range(len(board)):
                if move == j + 1 and board[i][j]:
                    if len(stack) > 0 and board[i][j] == stack[-1]:
                        stack.pop()
                        answer += 2
                    else:
                        stack.append(board[i][j])
                    board[i][j] = 0
                    break
    
    return answer



# 2중 for문
# moves의 값이 열값이 될 수 있음을 활용
def solution2(board, moves):
    stack = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]:
                if len(stack) > 0 and board[j][i-1] == stack[-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer

print(solution2([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))