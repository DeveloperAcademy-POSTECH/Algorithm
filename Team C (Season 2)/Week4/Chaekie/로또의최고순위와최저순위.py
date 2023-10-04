def check_fail(number):
    rank = 7 - number
    if rank > 6:
        return 6
    else:
        return rank

def solution1(lottos, win_nums):
    answer = []
    unknown = len(list(filter(lambda number: number == 0, lottos)))
    lottos_dict = {lotto: 0 for lotto in lottos}
    result = 0

    for num in win_nums:
        if num in lottos_dict:
            result += 1

    answer = [check_fail(result+unknown), check_fail(result)]

    return answer

# 그냥 count 써주면 됨...
# answer랑 rank의 인덱스값 연결해주면 됨
def solution2(lottos, win_nums):
    rank=[6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    answer = 0
    for number in win_nums:
        if number in lottos:
            answer += 1
    return rank[cnt_0 + answer],rank[answer]