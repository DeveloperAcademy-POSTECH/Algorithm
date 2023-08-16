# https://school.programmers.co.kr/learn/courses/30/lessons/62048
# 프로그래머스 - 멀쩡한 사각형

def gcd(x,y):
    if x==y:
        return x
    elif x>y: 
        return y if x%y==0 else gcd(y, x%y)
    else: 
        return x if y%x==0 else gcd(x,y%x)

def solution(w,h):
    return w*h - (w+h-gcd(w,h))