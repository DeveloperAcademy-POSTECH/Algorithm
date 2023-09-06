#완전탐색_카펫
def solution(brown, yellow):
    index = (brown - 4) / 2
    answer = []

    for i in range(1, int(index/2)+1):
        carpet = i * (index - i)
        if carpet == yellow:
            answer.append(index-i+2)
            answer.append(i+2)

    return answer