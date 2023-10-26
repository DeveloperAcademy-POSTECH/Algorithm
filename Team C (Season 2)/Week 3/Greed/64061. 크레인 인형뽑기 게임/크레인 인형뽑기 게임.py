def solution(board, moves):
    stack = [0]
    answer = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                top = stack[-1]
                if top == board[j][i-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer