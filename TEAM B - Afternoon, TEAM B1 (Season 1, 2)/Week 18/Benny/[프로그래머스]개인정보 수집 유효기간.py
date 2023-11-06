# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 개인정보 수집 유효기간

def convert_to_day(date):
    year, month, day = map(int, date.split("."))
    converted = (year - 2000) * 12 * 28 + (month - 1) * 28 + (day - 1)
    return converted

def preprocess_privacy(privacy):
    date, term = privacy.split()
    date = convert_to_day(date)
    return [date, term]
    

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    for t in terms:
        term, period = t.split()
        terms_dict[term] = int(period) * 28
        
    privacies = list(map(preprocess_privacy, privacies))
    today = convert_to_day(today)
    
    for i in range(len(privacies)):
        privacy_date, term = privacies[i]
        if privacy_date + terms_dict[term] <= today:
            answer.append(i+1)
    
    return answer