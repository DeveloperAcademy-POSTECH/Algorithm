def check_fail(number):
    rank = 7 - number
    if rank > 6:
        return 6
    else:
        return rank

def solution(lottos, win_nums):
    answer = []
    unknown = len(list(filter(lambda number: number == 0, lottos)))
    lottos_dict = {lotto: 0 for lotto in lottos}
    result = 0

    for num in win_nums:
        if num in lottos_dict:
            result += 1

    answer = [check_fail(result+unknown), check_fail(result)]

    return answer