score = {i:0 for i in ["R", "T", "C", "F", "J", "M", "A", "N"]}

def scoring(survey, choice):
    if choice == 4:
        return
    elif choice > 4:
        score[survey[1]] += choice-4
    else:
        score[survey[0]] += 4-choice

def solution(survey, choices):
    answer = ''
    
    # scoring with choices
    for i in range(len(choices)):
        scoring(survey[i], choices[i])

    # select type that has higher score
    if score["R"] >= score["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if score["C"] >= score["F"]:
        answer += "C"
    else:
        answer += "F"
    
    if score["J"] >= score["M"]:
        answer += "J"
    else:
        answer += "M"
    
    if score["A"] >= score["N"]:
        answer += "A"
    else:
        answer += "N"
        
    return answer