from itertools import combinations_with_replacement as cwr
def solution(n, info):
    answer = [-1]
    maxscore = 0
    for i in list(cwr(range(0,11), n)):
        temprion = [0]*11
        for j in i:
            temprion[10-j] += 1
        rionscore, appeachscore = 0, 0
        for k in range(0,11):
            if temprion[k]>info[k]:
                rionscore += 10-k
            elif info[k]:
                appeachscore += 10-k
        if rionscore - appeachscore > maxscore:
            maxscore = rionscore - appeachscore
            answer = temprion
    return answer