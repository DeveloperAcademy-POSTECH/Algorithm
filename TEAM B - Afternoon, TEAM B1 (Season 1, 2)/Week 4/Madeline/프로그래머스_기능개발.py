def solution(progresses, speeds):
    answer = [1]
    day = []
    # 각 작업 별 남은 일수
    for i in range(0, len(progresses)):
        j = 0
        cal = 0
        while (cal < 100):
            cal = progresses[i] + (speeds[i] * j)
            j += 1
        day.append(j - 1)

    # answer
    j = 0
    # 비교 대상
    former = day[0]
    for i in range(1, len(day)):
        if (day[i] <= former):
            answer[j] += 1
        else:
            answer.append(1)
            former = day[i]
            j += 1
    return answer
