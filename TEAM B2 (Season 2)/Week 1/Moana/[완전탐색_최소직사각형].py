# 완전탐색_최소 직사각형
def solution(sizes):
    width= 1
    height = 1
    for w,h in sizes:
        width = max(width, min(w,h))
        height = max(height, max(w,h))


    answer =  width * height
    return answer