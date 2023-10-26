def solution1(id_list, report, k):
    answer = []
    reporter_dict = {id: set() for id in id_list}
    attacker_dict = {id: set() for id in id_list}
    result_dict = {id: 0 for id in id_list}

    for case in report:
        reporter = case.split()[0]
        attacker = case.split()[1]
        reporter_dict[reporter].add(attacker) 
        attacker_dict[attacker].add(reporter) 

    for attacker in attacker_dict:
        if len(attacker_dict[attacker]) >= k:
            for reporter, attackers in reporter_dict.items():
                if attacker in attackers:
                    result_dict[reporter] += 1

    answer = list(result_dict.values())

    return answer



# report 자체를 set 해주면 됨
# id_list의 인덱스값을 이용해 reporter 이름이랑 매치함
def solution2(id_list, report, k):
    answer = [0] * len(id_list)    
    report_dict = {id : 0 for id in id_list}

    for reporter in set(report):
        report_dict[reporter.split()[1]] += 1

    for reporter in set(report):
        if report_dict[reporter.split()[1]] >= k:
            answer[id_list.index(reporter.split()[0])] += 1

    return answer