def solution(survey, choices):
    answer = ""
    personaldict = {
        "R" : 0,
        "T" : 0,
        "C" : 0,
        "F" : 0,
        "J" : 0,
        "M" : 0,
        "A" : 0,
        "N" : 0
    }
    point = [-100,3,2,1,0,1,2,3]
    for i in range(len(survey)):
        if(choices[i]>4):
            personaldict[survey[i][1]] += point[choices[i]]
        else:
            personaldict[survey[i][0]] += point[choices[i]]
    answer += "R" if personaldict["R"]>=personaldict["T"] else "T"
    answer += "C" if personaldict["C"]>=personaldict["F"] else "F"
    answer += "J" if personaldict["J"]>=personaldict["M"] else "M"
    answer += "A" if personaldict["A"]>=personaldict["N"] else "N"
    return answer