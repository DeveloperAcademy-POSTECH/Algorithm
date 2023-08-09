# https://www.acmicpc.net/problem/14888
# 백준-14888-연산자 끼워넣기

# 풀이1
import sys

def operate(a, b, operator):
    if operator == 0:
        return a + b
    elif operator == 1:
        return a - b
    elif operator == 2:
        return a * b
    elif a * b < 0:
        return a // b if a % b == 0 else a // b + 1
    else:
        return a // b
            

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers.reverse()
operators = list(map(int, input().split()))

max_value = -1_000_000_000
min_value = 1_000_000_000

def dfs(numbers, operators, max_value, min_value):
    if len(numbers) >= 2:
        for i in range(4):
            if operators[i] > 0:
                a = numbers.pop()
                b = numbers.pop()
                numbers.append(operate(a, b, i))
                operators[i] -= 1
                temp_max_value, temp_min_value = dfs(numbers, operators, max_value, min_value)
                max_value = max(max_value, temp_max_value)
                min_value = min(min_value, temp_min_value)
                operators[i] += 1
                numbers.pop()
                numbers.append(b)
                numbers.append(a)
            
        return max_value, min_value
    else:
        return numbers[0], numbers[0]
    
max_value, min_value = dfs(numbers, operators, max_value, min_value)
print(max_value)
print(min_value)

# 풀이2
# https://www.acmicpc.net/problem/14888
# 백준-14888-연산자 끼워넣기

import sys
from collections import deque

def operate(a, b, operator):
    if operator == 0:
        return a + b
    elif operator == 1:
        return a - b
    elif operator == 2:
        return a * b
    elif a * b < 0:
        return a // b if a % b == 0 else a // b + 1
    else:
        return a // b
            

input = sys.stdin.readline

n = int(input())
numbers = deque(map(int, input().split()))
operators = list(map(int, input().split()))

max_value = -1_000_000_000
min_value = 1_000_000_000

def dfs(numbers, operators, max_value, min_value):
    if len(numbers) >= 2:
        for i in range(4):
            if operators[i] > 0:
                a = numbers.popleft()
                b = numbers.popleft()
                numbers.appendleft(operate(a, b, i))
                operators[i] -= 1
                temp_max_value, temp_min_value = dfs(numbers, operators, max_value, min_value)
                max_value = max(max_value, temp_max_value)
                min_value = min(min_value, temp_min_value)
                operators[i] += 1
                numbers.popleft()
                numbers.appendleft(b)
                numbers.appendleft(a)
            
        return max_value, min_value
    
    else:
        return numbers[0], numbers[0]
    
max_value, min_value = dfs(numbers, operators, max_value, min_value)
print(max_value)
print(min_value)
'''
풀이 1, 2 모두 논리는 같습니다. 입력받은 숫자 순서대로 넣고 연산기호를 바꿔가며 넣습니다.
연산은 문제 조건대로 구현했습니다. 원래는 '0으로 나눠질 수 없다'라는 조건이 있어야 하지만 이 문제에선 그런 경우에 대한 언급이 없으므로 0으로 나눠지는 경우는 없도록 input이 들어온다고 판단했습니다.

풀이1은 deque를 이용했고 풀이2는 list를 이용했습니다.
list를 이용할 경우 pop(), append()만이 O(1)의 시간복잡도를 가지므로 수열의 순서를 거꾸로 바꾸었습니다.
'''