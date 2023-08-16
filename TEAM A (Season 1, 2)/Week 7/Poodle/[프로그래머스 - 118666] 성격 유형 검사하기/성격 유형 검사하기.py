scores = {}
scores['R'] = 0
scores['T'] = 0
scores['C'] = 0
scores['F'] = 0
scores['J'] = 0
scores['M'] = 0
scores['A'] = 0
scores['N'] = 0

def calculate(question, choice):
    A, B = list(question)
    
    if choice == 4: return
    elif choice < 4:
        scores[A] += abs(choice - 4)
    else:
        scores[B] += abs(choice - 4)

def solution(survey, choices):
    answer = ''
    
    for idx in range(len(survey)):
        calculate(survey[idx], choices[idx])
        
    # print(scores)
        
    answer += 'R' if scores['T'] - scores['R'] <= 0 else 'T'
    answer += 'C' if scores['F'] - scores['C'] <= 0 else 'F'
    answer += 'J' if scores['M'] - scores['J'] <= 0 else 'M'
    answer += 'A' if scores['N'] - scores['A'] <= 0 else 'N'
    
    return answer
