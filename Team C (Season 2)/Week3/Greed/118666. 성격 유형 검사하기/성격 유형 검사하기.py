def solution(survey, choices):
    characters = ["R","T","C","F","J","M","A","N"]
    score = [0]*len(characters)
    answer = []
    for i in range(len(survey)):
        if choices[i] <4:
            for j in range(len(characters)):
                if characters[j] == survey[i][:1]:
                    score[j] += 4 - choices[i] 
        else:
            for j in range(len(characters)):
                if characters[j] == survey[i][1:]:
                    score[j] += choices[i] - 4 

    for i in range(0,len(characters),2):
        if score[i] > score[i+1]:
            answer.append(characters[i])
        elif score[i] < score[i+1]:
            answer.append(characters[i+1])
        else:
            answer.append(characters[i] if characters[i] < characters[i+1] else characters[i+1])
    print(answer)
    return "".join(answer)