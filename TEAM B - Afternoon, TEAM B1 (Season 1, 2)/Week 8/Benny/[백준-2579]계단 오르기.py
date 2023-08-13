#https://www.acmicpc.net/problem/2579
# 백준-2579-계단 오르기

import sys

input = sys.stdin.readline

n = int(input())

steps = []
for _ in range(n):
    steps.append([int(input())]*2)
    
if n == 1:
    print(steps[0][0])
    
elif n == 2:
    print(steps[0][0] + steps[1][0])
    
else:
    steps[1][1] += steps[0][0]
    for i in range(2, len(steps)):
        steps[i][0] += max(steps[i-2][0], steps[i-2][1])
        steps[i][1] += steps[i-1][0]

    print(max(steps[-1][0], steps[-1][1]))

'''
문제 조건에서 연속으로 세 번 계단을 밟을 수는 없다고 했습니다. 즉 스택은 두번까지 쌓일 수 있습니다. 이에 따라 두 가지 경우로 나눌 수 있습니다. 
지금 i번째 계단을 밟는다고 가정했을 때,
1) i번째 계단이 첫번쨰 스택인 경우(이전 계단과 이어서 연속되지 않았을 경우)
2) i번째 계단이 두번째 스택인 경우(이전 계단에 이어 연속으로 i번째 계단을 밟았을 경우)

두 가지 경우에 대한 정보를 계단마다 저장하기 위해 2차원 배열을 사용하고 이전의 계단들을 이용해 i번째 계단의 정보를 업데이트합니다.
'''