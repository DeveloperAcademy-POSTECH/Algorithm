from collections import Counter

def solution(nums):
    c = Counter(nums)
    answer = min(len(c), len(nums)//2)
    return answer