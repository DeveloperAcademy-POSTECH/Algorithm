def solution(participant, completion):
    answer = ""
    participant.sort()
    completion.sort()

    for part, comp in zip(participant, completion):
        if part != comp:
            answer = part
            break
            
    if answer == "":
        answer = participant[-1]

    return answer