# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s: str) -> bool:
    stack = []
    for char in s:
        if char == '(': # open
            stack.append(char)
        else: # closed
            if not stack: return False
            stack.pop()
    return True if not stack else False
        





# def solution(s):
#     if len(s) % 2: return False
#     cnt = 0
#     for b in s:
#         cnt = cnt+1 if b == '(' else cnt-1
#         if cnt < 0: return False
#     return False if cnt else True