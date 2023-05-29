def solution(today, terms, privacies):
    answer = []
    termList = {}
    for t in terms:
        termList[t.split()[0]] = int(t.split()[1])

    privList = []
    for p in privacies:
        privList.append(p.split())

    t_year = int(today[:4])
    t_month = int(today[5:7])
    t_day = int(today[8:10])

    for index, p in enumerate(privList):
        year = int(p[0][:4])
        month = int(p[0][5:7])
        day = int(p[0][8:10])
        c = p[1]

        # term에 따른 month 추가
        m = termList[c]

        month += m
        while month >= 13:
            month -= 12
            year += 1

        # 비교
        if t_year > year:
            answer.append(index+1)
            continue
        elif t_year == year:
            if t_month > month:
                answer.append(index+1)
                continue
            elif t_month == month:
                if t_day >= day:
                    answer.append(index+1)
                else:
                    continue
            else:
                continue
        else:
            continue

    return answer