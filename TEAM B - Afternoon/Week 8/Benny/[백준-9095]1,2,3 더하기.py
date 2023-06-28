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
        
        