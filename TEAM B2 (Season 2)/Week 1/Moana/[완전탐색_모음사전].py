#완전탐색_모음사전
def solution(word):
    answer = 0
    vowels = ["A", "E", "I", "O", "U"]
    digits = [781, 156, 31, 6, 1]
    for i in range(len(word)):
        answer += vowels.index(word[i]) * digits[i] + 1
    return answer