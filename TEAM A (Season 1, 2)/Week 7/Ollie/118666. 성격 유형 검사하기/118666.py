def solution(survey, choices):
    types = ["RT", "CF", "JM", "AN"]
    dict = { type: 0 for type in types }
    for type, score in zip(survey, choices):
        # score = score - 4 if type[0] < type[1] else -score + 4
        # type = type if type[0] < type[1] else type[::-1]
        if type in dict: score = score - 4
        else: score, type = -score + 4, type[::-1]
        dict[type] += score
    
    return "".join([type[1] if dict[type] > 0 else type[0] for type in types])