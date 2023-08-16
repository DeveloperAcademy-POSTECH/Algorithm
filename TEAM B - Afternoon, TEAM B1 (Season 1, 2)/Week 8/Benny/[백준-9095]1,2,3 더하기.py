# https://www.acmicpc.net/problem/9095
# 백준-9095-1,2,3 더하기

import sys

input = sys.stdin.readline

t = int(input())
cases = []
for _ in range(t):
    cases.append(int(input()))
    
answers = [0, 1, 2, 4]
for i in range(4, max(cases)+1):
    answers.append(answers[i-3] + answers[i-2] + answers[i-1])
    
for case in cases:
    print(answers[case])
        

'''
어떤 수 N에 대해서 N을 가장 앞의 수 or 가장 뒤의 수와 그 수를 제외한 나머지 수로 나눌 수 있습니다.
가장 앞의 수와 나머지로 나눈다고 가정해보겠습니다.
가장 앞의 수는 1, 2, 3 중 하나입니다. 
예를 들어 가장 앞의 수가 1이라면 나머지 숫자의 합은 N-1입니다. 즉 N-1을 표현하는 가짓수와 같습니다.
마찬가지로 가장 앞의 수가 2, 3일 때는 각각 N-2, N-3 표현과 같습니다.

따라서 N을 표현하는 방식의 수는 N-1을 표현하는 방식의 수 + N-2를 표현하는 방식의 수 + N-3을 표현하는 방식의 수와 같습니다.
'''