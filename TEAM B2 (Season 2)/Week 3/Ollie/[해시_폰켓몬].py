
# 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
from typing import List
from collections import Counter

def solution(nums: List[int]) -> int:
    c = Counter(nums)
    return min(len(nums) / 2, len(c))