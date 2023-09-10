# 백준 1360번: 되돌리기

import sys

input = sys.stdin.readline

# N <= 10^2
N = int(input())

# 단위 명령마다 가장 오래 걸릴 수 있는 시간을 고려하면
# type: O(1)
# undo: O(N)
# 관건은 undo 명령의 중복을 어떻게 효율적으로 처리할 수 있을까?

commands = [input().rstrip().split() for _ in range(N)]

answer = ''

while commands:
    opcode, operand, T = commands.pop()

    if opcode == 'type':
         answer = operand + answer
    elif opcode == 'undo':
         reset_head = int(T) - int(operand)

         while commands and reset_head <= int(commands[-1][2]):
              _ = commands.pop()

print(answer)
