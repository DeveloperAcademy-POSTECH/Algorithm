import math

def solution(clothes):
    # 질문하기 참고 후 다시 풀어봄
    c_dict = {}
    for _, ctype in clothes:
        c_dict[ctype] = c_dict[ctype]+1 if ctype in c_dict else 2
    return math.prod(c_dict.values()) - 1