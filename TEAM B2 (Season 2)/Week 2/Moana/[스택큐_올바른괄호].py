def solution(s):
    answer = True
    parentheses = list(s)
    tmp = 0
    
    for i in range(len(parentheses)):
        if answer == False:
            break
            
        if parentheses[i] == "(":
            tmp += 1
        elif parentheses[i] == ")":
            if tmp > 0:
                tmp -= 1
            else:
                answer = False
        
       
    if tmp != 0:
        answer = False
        
    return answer