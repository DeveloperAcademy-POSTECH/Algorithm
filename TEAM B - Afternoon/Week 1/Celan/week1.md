## Stack Queue

- [6198/옥상정원꾸미기](https://github.com/ValseLee/algorithm_study/blob/main/%EB%B0%B1%EC%A4%80/Gold/6198.%E2%80%85%EC%98%A5%EC%83%81%E2%80%85%EC%A0%95%EC%9B%90%E2%80%85%EA%BE%B8%EB%AF%B8%EA%B8%B0/%EC%98%A5%EC%83%81%E2%80%85%EC%A0%95%EC%9B%90%E2%80%85%EA%BE%B8%EB%AF%B8%EA%B8%B0.py)

```py
# N=6, H = {10, 3, 7, 4, 12, 2}
import sys

N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]
stack, res = [], 0
for i in range(N):
    while stack != [] and stack[-1] <= li[i]:
        stack.pop()
    stack.append(li[i])
    res += len(stack)-1
print(res)
```

- [10828/스택](https://github.com/ValseLee/algorithm_study/blob/main/%EB%B0%B1%EC%A4%80/Silver/10828.%E2%80%85%EC%8A%A4%ED%83%9D/%EC%8A%A4%ED%83%9D.py)
```py
stack = []
k = int(input())
arr = [input() for _ in range(k)]

for i in arr:
    com = i.split(' ')
    if com[0]=='push':
        stack.append(com[1])
    elif com[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif com[0] == 'size':
        print(len(stack))
    elif com[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])    
        
```

- [10773/제로](https://github.com/ValseLee/algorithm_study/blob/main/%EB%B0%B1%EC%A4%80/Silver/10773.%E2%80%85%EC%A0%9C%EB%A1%9C/%EC%A0%9C%EB%A1%9C.py)
```py
k = int(input())
arr = [int(input()) for _ in range(k)]
stack = []

for i in arr:
    if i != 0:
        stack.append(i)
    if i == 0:
        stack.pop()
        
print(sum(stack))
```

- [lv2/올바른 괄호](https://github.com/ValseLee/algorithm_study/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/lv2/12909.%E2%80%85%EC%98%AC%EB%B0%94%EB%A5%B8%E2%80%85%EA%B4%84%ED%98%B8/%EC%98%AC%EB%B0%94%EB%A5%B8%E2%80%85%EA%B4%84%ED%98%B8.py)

```py
def solution(s):
    stack = []
    
    for parens in s:
        if parens == '(':
            stack.append(parens)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
    
    return True if stack == [] else False
```

- [lv2/프로세스](https://github.com/ValseLee/algorithm_study/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/lv2/42587.%E2%80%85%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4/%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4.py)

```py
def solution(priorities, location):
    queue = [(v, idx) for idx, v in enumerate(priorities)]
    answer = 0
    
    while True:
        if queue[0][0] == max(queue)[0]:
            answer += 1
            if queue[0][1] == location:
                break
            queue.pop(0)
        else:
            queue.append(queue.pop(0))
            
    return answer
```
