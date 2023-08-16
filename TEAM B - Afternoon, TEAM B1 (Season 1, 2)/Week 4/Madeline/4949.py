#4949
# . = 입력 종료 조건
# 스택 문제 = 열린 괄호 == 스택에 넣고, 닫힌 괄호 == 스택에서 pop

# 이 문제에서는 sys.stdin.readline 를 사용하면 출력 초과가 뜬당,,
# -> readline = 개행 문자 포항해서 입력받는다.
# input = 자동으로 개행문자를 지워서 입력받는다.

# import sys

# input = sys.stdin.readline

while(1):
    str = input()
    stack = []  # 리스트

    if str == '.':  # 종료조건
        break

    for i in str:
        if i == '[': # 괄호 시작 시 스택에 저장
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[': # stack이 비어있지 않고, 마지막이 [ 일때 => 균형이 맞아
                stack.pop()
            else:   # stack이 비어있거나, 짝이 안맞으면 ] 를 추가하고 break
                stack.append(i)
                break
        elif i == '(': # 괄호 시작 시 스택에 저장
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(': # stack이 비어있지 않고, 마지막이 ( 일때 => 균형이 맞아
                stack.pop()
            else:
                stack.append(i) # stack이 비어있거나, 짝이 안맞으면 ] 를 추가하고 break
                break
    if stack:   # stack이 비어있지 않음 = 균형이 안맞음
        print("no")
    else:
        print("yes")


