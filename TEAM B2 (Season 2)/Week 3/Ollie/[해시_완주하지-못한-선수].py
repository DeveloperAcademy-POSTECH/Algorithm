
# 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
from typing import List

def solution(participant: List[str], completion: List[str]) -> str:
    completionDictionary = dict()
    for comp in completion:
        if comp in completionDictionary:
            completionDictionary[comp] += 1
        else:
            completionDictionary[comp] = 1
    for part in participant:
        if part not in completionDictionary:
            return part
        else:
            if completionDictionary[part] == 1:
                del completionDictionary[part]
            else:
                completionDictionary[part] -= 1
    return ""