# https://www.acmicpc.net/problem/9093
# 백준-9093-단어 뒤집기

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    print(' '.join(map(lambda x: x[::-1], sys.stdin.readline().split())))

'''
공백 기준으로 단어를 분리하고 각 단어를 lambda 함수를 통해 뒤집습니다.
'''
    