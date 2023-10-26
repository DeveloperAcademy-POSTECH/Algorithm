def solution(n, lost, reserve):
    cloth = [1] * (n+1)
    cloth[0] = 0

    for student in reserve:
        cloth[student] += 1
        
    for student in lost:
        cloth[student] -= 1
        
    for i in range(len(cloth)):
        if i == 0:
            continue
        if cloth[i] == 0 and cloth[i-1] == 2:
            cloth[i] = 1
            cloth[i-1] = 1
        if i+1 <= n:
            if cloth[i] == 0 and cloth[i+1] == 2:
                cloth[i] = 1
                cloth[i+1] = 1
    
    answer = len(cloth) - cloth.count(0)
    return answer