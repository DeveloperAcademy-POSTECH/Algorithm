# https://www.acmicpc.net/problem/1107
# 백준-1107-리모컨

import sys

input = sys.stdin.readline

def check_brokens(num):
    global brokens
    # brokens의 최대 길이는 10. 따라서 최대 10번의 연산 수행
    for b in brokens: 
        # str()은 num의 자릿수만큼 연산을 수행하게 됨. num <= 500,000이므로 최대 6번의 연산 수행
        if b in str(num):
            return True
    return False

n = input()
m = input()
brokens = input().split()

if int(n) == 100:
    print(0)
    
elif int(n) > 100:
    min_count = int(n) - 100
    
    cur = int(n)
    
    # 각 while문은 최대 N-100번 정도 돌게 됨.
    while check_brokens(cur):
        cur -= 1
        if cur <= 100: 
            break
            
    if not check_brokens(cur):
        count = int(n) - cur + len(str(cur))
        min_count = min(min_count, count)
    
    cur = int(n)
    while check_brokens(cur):
        cur += 1
        if cur >= int(n) + int(n) - 100: 
            break

    if not check_brokens(cur):
        count = cur - int(n) + len(str(cur))
        min_count = min(min_count, count)
    
    print(min_count)
    
else:
    min_count = 100 - int(n)
    cur = int(n)
    while check_brokens(cur):
        cur -= 1
        if cur <= 0:
            break

    if not check_brokens(cur):
        count = int(n) - cur + len(str(cur))
        min_count = min(min_count, count)
    
    cur = int(n)
    while check_brokens(cur):
        cur += 1
        if cur >= 100:
            break
    
    if not check_brokens(cur):
        count = cur - int(n) + len(str(cur))
        min_count = min(min_count, count)
    
    print(min_count)