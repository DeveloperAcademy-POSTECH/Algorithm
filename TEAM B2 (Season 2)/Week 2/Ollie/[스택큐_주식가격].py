# 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584
from typing import List

# [1, 2, 3, 2, 3] 	[4, 3, 1, 1, 0]
def solution(prices: List[int]) -> List[int]:
    stack = []
    answer = [0] * len(prices)
    for index, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            pointer, _ = stack.pop()
            answer[pointer] = index - pointer
        stack.append((index, price))
    for index, _ in stack:
        answer[index] = len(prices) - index - 1
    return answer





# def solution(prices):
#     s = []
#     answer = [0] * len(prices)
#     for idx, price in enumerate(prices[:-1]):
#         while s and s[-1][1] > price:
#             p, _ = s.pop()
#             answer[p] = idx - p
#         s.append([idx, price])
#     for idx, _ in s:
#         answer[idx] = len(prices) - 1 - idx
#     return answer