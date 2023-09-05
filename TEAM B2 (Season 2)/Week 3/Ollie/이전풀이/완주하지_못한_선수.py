# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()
    while completion:
        a = participant.pop()
        b = completion.pop()
        if a != b:
            return a
    return participant.pop()