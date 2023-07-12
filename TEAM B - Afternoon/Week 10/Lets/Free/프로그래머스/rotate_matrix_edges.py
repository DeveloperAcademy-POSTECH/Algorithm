# https://school.programmers.co.kr/learn/courses/30/lessons/77485

# 1에서 n까지 적혀있는 행렬
# 회전시킬 테두리의 상단 하단 좌표를 줌
# 회전에 의해 위치가 바뀐 숫자들을 작은 순서대로 반환

answer = []

def spin(matrix, querie):
    x1, y1, x2, y2 = querie
    x1, x2, y1, y2 = x1-1, x2-1, y1-1, y2-1
    garo = y2-y1
    cero = x2-x1
    
    min_num = 100000
    
    row, col = len(matrix), len(matrix[0])
    
    # 행렬 복사
    n_matrix = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            n_matrix[i][j] = matrix[i][j]
            
    
    direction = 0
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    r, c = x1, y1
    
    while direction < 4:
        move = 0
        
        if direction % 2: # 세로로 이동
            while move < cero: # 끝에서 한칸 전까지의 값을 이동
                nr = r + dr[direction]
                nc = c + dc[direction]
                
                # 최소숫자
                if matrix[r][c] < min_num:
                    min_num = matrix[r][c]
                
                # 이동
                n_matrix[nr][nc] = matrix[r][c]
                
                # 시작 좌표 변경
                r = nr
                c = nc
                
                # 1번 이동했음을 표시
                move += 1
                
        else: # 가로로 이동
            while move < garo:
                nr = r + dr[direction]
                nc = c + dc[direction]
                
                # 최소숫자
                if matrix[r][c] < min_num:
                    min_num = matrix[r][c]
                
                # 이동
                n_matrix[nr][nc] = matrix[r][c]
                
                # 시작 좌표 변경
                r = nr
                c = nc
                
                # 1번 이동했음을 표시
                move += 1
        
        direction += 1
        
    global answer
    answer.append(min_num)
        
    return n_matrix

def solution(rows, columns, queries):
    # 행렬은 완성
    matrix = [[column+columns*row + 1 for column in range(columns)] for row in range(rows)]
    
    # 이제 돌려야함
    for querie in queries:
        result_matrix = spin(matrix, querie)
        
        # 돌린것을 기준 행렬로 만들어줌
        matrix = result_matrix
        
    print(matrix)    
    return answer