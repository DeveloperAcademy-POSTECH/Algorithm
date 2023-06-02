def solution(today, terms, privacies):
    termDict = {}
    answer =[]
    todayyear, todaymonth, todayday = int(today[0:4]), int(today[5:7]), int(today[8:])
    for i in terms:
        termDict[i[0]] = int(i[2:])
    for index, j in enumerate(privacies):
        uhogigan = termDict[j[-1]] 
        year,month,day = int(j[0:4]), int(j[5:7]),int(j[8:10]) 
        aftermonth = month + uhogigan
        while(aftermonth>12):
            year+=1
            aftermonth -= 12
        if(year>todayyear): #이미 유효기간이 개인정보년보다 길면
            continue
        elif(year==todayyear):
            if(aftermonth>todaymonth):
                continue
            elif(aftermonth == todaymonth):
                if(todayday<day):
                    continue
        answer.append(index+1)
    return answer