def solution(id_list, report, k):
    # 정지 성공한 횟수 저장
    answer = [0]*len(id_list)
    # 신고당한 횟수 저장
    dict = {id : 0 for id in id_list}
    
    for i in set(report):
        dict[i.split()[1]] += 1

    for i in set(report):
        if dict[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1
    return answer