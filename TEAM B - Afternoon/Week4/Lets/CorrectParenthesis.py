# 괄호의 갯수와 순서가 올바른지를 테스트 해야할듯
# 괄호 ( 만 스택에 넣고, ) 를 만나면 스택에서 빼는 방법으로
# 만약 진행과정중에 뭐라도 안된다? 바로 False

def solution(s):
    
    return checkParentheses(s)

def checkParentheses(s):
    stack = []
    for letter in s:
        if letter == "(":
            stack.append(letter)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
        
    ## 이건 내가짠건데 이 방법말고
    # if stack == []:
    #     return True
    # else:
    #     return False
    
    # 요게 더 예쁘다
    return len(stack) == 0