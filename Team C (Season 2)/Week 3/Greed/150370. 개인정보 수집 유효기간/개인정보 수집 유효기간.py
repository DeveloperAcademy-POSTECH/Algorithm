from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    format = '%Y.%m.%d'
    cnt = 0
    answer = []
    today = datetime.strptime(today, format)
    for i in range(len(privacies)):
        cnt += 1
        for j in range(len(terms)):
            privaciesInfo = privacies[i].split(' ')
            agreePeriod = terms[j].split(' ')[0]
            tmpAddMonth = terms[j].split(' ')[1]
            delta = relativedelta(months=int(tmpAddMonth))
            agreedDate = datetime.strptime(privaciesInfo[0], format)
            diff = agreedDate + delta
            if privaciesInfo[1] == agreePeriod and today >= diff:
                answer.append(cnt)
    return answer