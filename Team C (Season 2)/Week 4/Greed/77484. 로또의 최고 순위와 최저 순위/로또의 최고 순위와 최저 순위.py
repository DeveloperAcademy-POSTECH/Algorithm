def solution(lottos, win_nums):
    answer = []
    rank = 7
    zeroCnt = lottos.count(0)
    for i in lottos:
        for j in win_nums:
            if i == j:
                rank -= 1
    if rank == 7:
        rank = 6
    maxCorrectNum = rank - zeroCnt if zeroCnt != 6 else 1
    answer.append(maxCorrectNum)
    answer.append(rank)
    return answer