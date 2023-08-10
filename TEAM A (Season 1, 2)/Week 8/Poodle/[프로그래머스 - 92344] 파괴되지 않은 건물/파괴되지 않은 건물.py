def solution(board, skill):
    answer = 0
    
    N, M = len(board), len(board[0])
    
    prefix_sums = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        # print(f"{'Attack' if type == 1 else 'Heal'}, ({r1}, {c1}), ({r2}, {c2}), {degree}")
        
        # 적의 공격 스킬 처리
        if type == 1:
            prefix_sums[r1][c1] += -degree
            prefix_sums[r1][c2 + 1] += degree
            prefix_sums[r2 + 1][c1] += degree
            prefix_sums[r2 + 1][c2 + 1] += -degree
        # 아군의 회복 스킬 처리
        elif type == 2:
            prefix_sums[r1][c1] += degree
            prefix_sums[r1][c2 + 1] += -degree
            prefix_sums[r2 + 1][c1] += -degree
            prefix_sums[r2 + 1][c2 + 1] += degree
            
        # for row in prefix_sums:
        #     print(row)
        # print()
        
    # 열 누적합 처리
    for r in range(N):
        for c in range(M - 1):
            prefix_sums[r][c + 1] += prefix_sums[r][c]
    
    # 행 누적합 처리
    for r in range(N - 1):
        for c in range(M):
            prefix_sums[r + 1][c] += prefix_sums[r][c]
            
    # for row in prefix_sums:
    #     print(row)
    # print()
            
    # 누적합 배열을 반영
    for r in range(N):
        for c in range(M):
            board[r][c] += prefix_sums[r][c]
    
    # 남아 있는 건물 조사
    for row in board:
        # print(row)
        answer += len([i for i in row if i > 0])
    # print()
    
    return answer
