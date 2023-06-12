
def solution(survey, choices):
    type_dict = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}
    for q, choice in zip(survey, choices):
        if q not in type_dict.keys():
            type_dict[q[::-1]] += 4 - choice
        else:
            type_dict[q] += choice - 4
    
    res = []
    for k, v in type_dict.items():
        res.append(k[0] if v <= 0 else k[1])

    return ''.join(res)