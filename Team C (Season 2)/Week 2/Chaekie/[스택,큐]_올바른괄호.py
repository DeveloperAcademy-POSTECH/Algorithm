def solution(s):
    answer = [s[0]]
    for i in range(1, len(s)):
        if len(answer) != 0 and answer[-1] == "(" and s[i] == ")":
            answer.pop()
        else:
            answer.append(s[i])
            
    if len(answer) == 0:
        return True
    else:
        return False