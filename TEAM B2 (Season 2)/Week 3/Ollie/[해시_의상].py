
# 의상
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
from typing import List
import math

# [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]] 	5
def solution(clothes: List[List[str]]) -> int:
    dictionary = {}
    for _, clothes_type in clothes:
        if clothes_type in dictionary:
            dictionary[clothes_type] += 1
        else:
            dictionary[clothes_type] = 2
    return math.prod(dictionary.values()) - 1