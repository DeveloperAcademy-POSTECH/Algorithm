# https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3

def solution(sizes):
    maxWidth, maxHeight = 0, 0
    for (width, height) in sizes:
        if width <= height:
            width, height = height, width
        maxWidth = max(width, maxWidth)
        maxHeight = max(height, maxHeight)
    return maxWidth * maxHeight



# def solution(sizes):
#     b = max([i if i>j else j for i, j in sizes])
#     s = max([i if i <= j else j for i, j in sizes])
#     return b*s