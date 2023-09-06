import math

def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    median = int(math.sqrt(sum))
    if sum % median == 0:
            answer.append(sum // median)
            answer.append(median)
    else:
        for i in range(median):
            width = median - (i + 1)
            if sum % width == 0 and (width - 2) * (sum // width - 2) == yellow:
                answer.append(sum // width)
                answer.append(width)
                break
    return answer