def solution(s):
    arr = list(s)
    cnt = 0
    for i in arr:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -=  1
        if cnt < 0:
            return False
    return cnt == 0