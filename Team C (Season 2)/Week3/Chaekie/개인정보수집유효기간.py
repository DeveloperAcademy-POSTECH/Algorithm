from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    # now = datetime.strptime(today.replace('.', ''), "%Y%m%d")
    now = datetime.strptime(today, "%Y.%m.%d")
    terms_dct = {terms[i].split()[0]: int(terms[i].split()[1]) for i in range(len(terms))}
    
    for idx, privacie in enumerate(privacies):
        # start_date = datetime.strptime(privacie.split()[0].replace('.', ''), "%Y%m%d")
        start_date = datetime.strptime(privacie.split()[0], "%Y.%m.%d")
        term = privacie.split()[1]
        
        # if start_date + relativedelta(months=terms_dct[term]) - relativedelta(days=1) < now:
        if start_date + relativedelta(months=terms_dct[term]) <= now:
            answer.append(idx+1)
    return answer



# 라이브러리 없이 작성한 코드, 한달이 28일로 설정된 것 사용해 기간을 day로 통일
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution2(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire


print(solution2("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
