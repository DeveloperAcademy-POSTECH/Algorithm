from collections import deque

s = input()
s = deque(list(s))

deq = deque()

result = 0

for i, p in enumerate(s):
    # 여는 괄호
    if p == "[" or p == "(":
        deq.append(p)
    # 닫는 괄호
    else:
        if not deq:
            print(0)
            exit()
        
        if p == "]":
            temp = 0
            # 여는 괄호 '['가 뽑힐 때 까지 Pop하며, 숫자들을 더함.
            while deq:
                a = deq.pop()
                # 숫자인 지 확인
                if isinstance(a, int):
                    temp += a
                    # 여는 괄호가 없었다면, break.
                    if not deq:
                        print(0)
                        exit()
                else:
                    # 다른 괄호가 나오면, break.
                    if a != "[":
                        print(0)
                        exit()
                    
                    # 여는 괄호 뒤 바로 닫는 괄호라면, 3을 더하고 끝냄. 숫자가 나왔다면, 나온 숫자에 3을 곱해 더하고 끝냄.
                    if temp == 0:
                        temp = 3
                    else:
                        temp *= 3
                        
                    break
            deq.append(temp)
        
        else:   # p == ")"
            temp = 0
            # 여는 괄호 '('가 뽑힐 때 까지 Pop하며, 숫자들을 더함.
            while deq:
                a = deq.pop()
                # 숫자인 지 확인
                if isinstance(a, int):
                    temp += a
                    # 여는 괄호가 없었다면, break.
                    if not deq:
                        print(0)
                        exit()
                else:
                    # 다른 괄호가 나오면, break.
                    if a != "(":
                        print(0)
                        exit()
                    
                    # 여는 괄호 뒤 바로 닫는 괄호라면, 3을 더하고 끝냄. 숫자가 나왔다면, 나온 숫자에 3을 곱해 더하고 끝냄.
                    if temp == 0:
                        temp = 2
                    else:
                        temp *= 2
                        
                    break
            deq.append(temp)

# deq 내에 괄호가 남아 있다면, print(0)
for k in deq:
    if not isinstance(k, int):
        print(0)
        exit()
        
print(sum(deq))