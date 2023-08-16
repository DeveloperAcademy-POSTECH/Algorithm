MAX_R = 51
MAX_C = 51

group = [[False for _ in range(MAX_C)] for _ in range(MAX_R)]
cell = [[False for _ in range(MAX_C)] for _ in range(MAX_R)]
outputs = []

# 명령어의 최대 개수: 10^3
# 표의 모든 셀을 한 번씩 방문하는 경우 < 3 * 10^3
# 빡구현 ㄱㄱ

def execute(line):
    global cell, group
    
    opcode, *params = line.split()
    
    if opcode == 'UPDATE':
        if len(params) == 3:
            r, c, value = params

            # (r, c) 위치의 셀을 선택합니다.
            r, c = group[int(r)][int(c)]
            
            # 선택한 셀의 값을 value로 바꿉니다.
            cell[r][c] = value
            
        elif len(params) == 2:
            value_1, value_2 = params
            
            # value1을 값으로 가지고 있는 모든 셀을 선택합니다.
            for r in range(MAX_R):
                for c in range(MAX_C):
                    if cell[r][c] == value_1:
                        # 선택한 셀의 값을 value2로 바꿉니다.
                        cell[r][c] = value_2
            
    elif opcode == 'MERGE':
        r1, c1, r2, c2 = map(int, params)
        
        # 선택한 두 위치의 셀이 같은 셀일 경우 무시합니다.
        if r1 == r2 and c1 == c2: return

        r1, c1 = group[r1][c1]
        r2, c2 = group[r2][c2]

        ref_value = False

        # 두 셀 모두 값을 가지고 있을 경우 병합된 셀은 (r1, c1) 위치의 셀 값을 가지게 됩니다.
        if cell[r1][c1] and cell[r2][c2]:
            ref_value = cell[r1][c1]
        # 두 셀 중 한 셀이 값을 가지고 있을 경우 병합된 셀은 그 값을 가지게 됩니다.
        elif cell[r1][c1]:
            ref_value = cell[r1][c1]
        elif cell[r2][c2]:
            ref_value = cell[r2][c2]

        for r in range(MAX_R):
            for c in range(MAX_C):
                if group[r][c] == [r2, c2]:
                    group[r][c] = [r1, c1]

        cell[r1][c1] = ref_value
        
    elif opcode == 'UNMERGE':
        r, c = map(int, params)
        
        ref_r, ref_c = group[r][c]
        ref_value = cell[ref_r][ref_c]
            
        # 선택한 셀이 포함하고 있던 모든 셀은 프로그램 실행 초기의 상태로 돌아갑니다.
        for dr in range(MAX_R):
            for dc in range(MAX_C):
                if group[dr][dc] == [ref_r, ref_c]:
                    cell[dr][dc] = False
                    group[dr][dc] = [dr, dc]

        # 병합을 해제하기 전 셀이 값을 가지고 있었을 경우 (r, c) 위치의 셀이 그 값을 가지게 됩니다.
        cell[r][c] = ref_value
        
    elif opcode == 'PRINT':
        global outputs
        
        r, c = map(int, params)
        r, c = group[r][c]
        
        # (r, c) 위치의 셀을 선택하여 셀의 값을 출력합니다.
        if cell[r][c]:
            outputs.append(cell[r][c])
        # 선택한 셀이 비어있을 경우 "EMPTY"를 출력합니다.
        else:
            outputs.append('EMPTY')

    return

def solution(commands):
    global group, outputs

    # group 리스트 초기화
    for r in range(MAX_R):
        for c in range(MAX_C):
            group[r][c] = [r, c]
    
    for line in commands:
        execute(line)
        
        # print(line)
        # print("----- VALUES -----")
        # for r in range(1, 3):
        #     for c in range(1, 3):
        #         print(cell[r][c], end=" ")
        #     print()
        # print("----- GROUPS -----")
        # for r in range(1, 3):
        #     for c in range(1, 3):
        #         print(group[r][c], end=" ")
        #     print()
        # print()
    
    return outputs
