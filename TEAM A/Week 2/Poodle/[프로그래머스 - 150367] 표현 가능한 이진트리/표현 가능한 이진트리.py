def solution(numbers):
    answer = []
    
    # 이진트리에 더미노드를 추가해 살펴본 그림을 참고하면, infix traversal을 수행함
    # 되는 것들 리스트
    # 7 -> 111 -> 111
    # 42 -> 101010 -> 0101010
    # 63 -> 111111 -> 0111111
    # 111 -> 64 + 32 + 8 + 4 + 2 + 1 -> 1101111 -> 1101111
    # 안되는 것들 리스트
    # 5 -> 101 -> 101
    # 95 -> 64 + 16 + 8 + 4 + 2 + 1 -> 1011111 -> 1011111
    
    # -> 1차로 해야 할 것: zero padding
    def traversal(idx, parent, step):
        # print(f"{idx}, {parent}, {bin_num[idx]}")

        flag = True
        current = bin_num[idx]

        # 리프 노드인 경우 -> 부모가 0이고 자식이 1인지만 검사
        if step == 1:
            if parent == '0' and current == '1':
                return False
            else:
                return True
        # 리프 노드가 아닌 경우
        else:
            new_step = step // 2
            
            if current == '1':
                if parent == '0': return False
                else:
                    flag = flag and traversal(idx - new_step, '1', new_step)
                    flag = flag and traversal(idx + new_step, '1', new_step)
            else:
                flag = flag and traversal(idx - new_step, '0', new_step)
                flag = flag and traversal(idx + new_step, '0', new_step)

        return flag
    
    for number in numbers:
        # 1에 대한 예외 처리를 쉽게 조건으로 남겨 놓기
        if number == 1:
            answer.append(1)
            continue
        
        # zero padding
        bin_num = bin(number)[2:]
        digits = 4
        depth = 2
        while digits - 1 < len(bin_num):
            digits *= 2
            depth += 1
        bin_num = bin_num.zfill(digits - 1)
        middle = len(bin_num) // 2
        
        answer.append(1 if traversal(middle, '1', middle + 1) else 0)

    return answer
