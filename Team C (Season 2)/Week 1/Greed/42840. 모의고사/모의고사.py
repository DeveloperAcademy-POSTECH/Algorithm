def solution(answers):
    count = len(answers)
    cnt = [0,0,0]
    # for i in range(count):
    #    sol1.append(i%5+1)
    #    if sol1[i] == answers[i]:
    #        cnt1 += 1
    # tmp = [1 % 5 + 1 for i in range(count)] 위와 같은 식이라고 함..
    #sol2 = [tmp2[i % 7] for i in range(count)]
    #sol3 = [tmp3[i % 9] for i in range(count)]
    tmp1 = [1,2,3,4,5]
    tmp2 = [2,1,2,3,2,4,2,5]
    tmp3 = [3,3,1,1,2,2,4,4,5,5]
   
    for i in range(len(answers)):
        if tmp1[i % 5] == answers[i]:
            cnt[0] += 1
        if tmp2[i % 8] == answers[i]:
            cnt[1] += 1
        if tmp3[i % 10] == answers[i]:
            cnt[2] += 1
    
    maxNum = max(cnt)
    answer = []

    for i in range(len(cnt)):
        if cnt[i] == maxNum:
            answer.append(i + 1)

    return answer